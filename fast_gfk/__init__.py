"""We use the word "target" to denote the value of the generic foreign key."""

class Wrapper(object):
    # todo: wrapper needs to return __class__ of wrapped context, not self

    def __init__(self, context, target, target_field="target"):
        self._context = context
        self._target = target
        self._target_field = target_field

    def __getattr__(self, name):
        if name == self._target_field:
            return self._target
        try:
            return super(Wrapper, self).__getattr__(name)
        except AttributeError:
            return getattr(self._context, name)


def fetch(queryset, field="content_object"):

    # Late import to avoid apps not loaded error
    from django.contrib.contenttypes.models import ContentType

    # Key is content type id, value is object id
    map_ct_targets = {}

    # Key one is content type id, key two is object id, value is a list of
    # items.
    map_two_deep = {}

    # Populate the dictionaries
    for obj in queryset:
        gfk_field = obj._meta.get_field(field)
        ct_id = getattr(obj, gfk_field.ct_field + "_id")
        obj_id = getattr(obj, gfk_field.fk_field)

        # map_ct_targets
        if ct_id not in map_ct_targets:
            map_ct_targets[ct_id] = []
        map_ct_targets[ct_id].append(obj_id)

        # map_two_deep
        if ct_id not in map_two_deep:
            map_two_deep[ct_id] = {}
        if obj_id not in map_two_deep[ct_id]:
            map_two_deep[ct_id][obj_id] = []
        map_two_deep[ct_id][obj_id].append(obj)

    # Pre-lookup the content types
    content_types = {}
    for ct in ContentType.objects.filter(id__in=map_ct_targets.keys()):
        content_types[ct.id] = ct

    # Map the targets onto the original objects by using a wrapper pattern
    wrapped_objects = {}
    for ct_id, ids in map_ct_targets.items():
        for obj in content_types[ct_id].model_class().objects.filter(id__in=ids):
            for item in map_two_deep[ct_id][obj.id]:
                wrapped_objects[item.id] = Wrapper(item, target=obj)

    # Yield the resulting list
    for obj in queryset:
        yield wrapped_objects[obj.id]

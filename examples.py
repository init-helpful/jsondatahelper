from jsondatahelper import flatten, unflatten, format_dict


#Standard dictionary
DICTIONARY_EXAMPLE = {
    "example": {
        "flattened": {"dictionary": "With A Value"},
        "with": {
            "index": [
                {"object_id": "id0", "object_name": "name0"},
                {"object_id": "id1", "object_name": "name1"},
            ]
        },
    }
}

FLATTEND_EXAMPLE = {
    "example->flattened->dictionary": "With A Value",
    "example->with->index->0->object_name": "name0",
    "example->with->index->0->object_id": "id0",
    "example->with->index->1->object_name": "name1",
    "example->with->index->1->object_id": "id1",
}


print(f"Standard -> Flattned\n{format_dict(flatten(DICTIONARY_EXAMPLE))}")

print(f"Flattned -> Standard\n{format_dict(unflatten(FLATTEND_EXAMPLE))}")

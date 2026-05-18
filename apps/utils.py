def extract_post_data(request, *fields):
    data = {}
    preserve_fields = {"password", "confirm_password"}
    for field in fields:
        value = request.POST.get(field, "")
        if field not in preserve_fields and isinstance(value, str):
            value = value.strip()
        data[field] = value
    return data
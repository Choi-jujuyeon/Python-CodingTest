def solution(data, ext, val_ext, sort_by):
    order=["code","date","maximum","remain"]
    sort_by = order.index(sort_by)
    ext = order.index(ext)
    arr=[i for i in data if i[ext]<val_ext]
    return sorted(arr, key=lambda x: x[sort_by])
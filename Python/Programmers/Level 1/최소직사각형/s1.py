def solution(sizes):
    mw = sizes[0][0]
    mh = sizes[0][1]
    for size in sizes[1:]:
        w, h = size[0], size[1]
        a = max(mw, w) * max(mh, h)
        b = max(mw, h) * max(mh, w)
        if a > b:
            mw, mh = max(mw, h), max(mh, w)
        else:
            mw, mh = max(mw, w), max(mh, h)
    return mw * mh

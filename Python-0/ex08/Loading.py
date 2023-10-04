def ft_tqdm(lst: range) -> None:
    """recreating the tqdm function which takes the range
and displays the loading bar"""
    length = len(lst)
    for x in lst:
        percent = (x / length) * 100
        bar = '◼️' * int(percent) + ' ' * (100 - int(percent))
        print(f"{percent:.0F}%|{bar}| {x}/{length}", end='\r')
        yield x
    bar = '◼️' * 100
    print(f"100%|{bar}| {length}/{length}")

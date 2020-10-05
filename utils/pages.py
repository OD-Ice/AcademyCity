
def pages_process(paginator, page_obj, around_num):
    total_pages = paginator.num_pages  # 总页码
    display_pages = 2 * around_num + 1  # 展示的页码数量
    current_page = page_obj.number  # 当前的页码

    if total_pages >= display_pages:
        if current_page <= around_num:
            left_pages = range(1, current_page)
            right_pages = range(current_page + 1, display_pages + 1)
        else:
            if current_page > total_pages - around_num:
                left_pages = range(total_pages - display_pages + 1, current_page)
                right_pages = range(current_page + 1, total_pages + 1)
            else:
                left_pages = range(current_page - around_num, current_page)
                right_pages = range(current_page + 1, current_page + around_num + 1)
    else:
        left_pages = range(1, current_page)
        right_pages = range(current_page + 1, total_pages + 1)

    return {
        'left_pages': left_pages,
        'right_pages': right_pages,
        'current_page': current_page
    }

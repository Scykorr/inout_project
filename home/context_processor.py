from home.models import HomePage


def main_menu_tree(request):
    main_menu = []
    home_page = HomePage.objects.all().select_related().first()
    if home_page:
        for page_item in home_page.get_children():
            if page_item.live and page_item.specific.show_main_menu:
                general_point_menu = {
                    'title': page_item.title,
                    'url': page_item.url,
                    'ordering': page_item.specific.ordering if hasattr(page_item.specific, 'ordering') else 10000
                }

                if page_item.get_children().count() > 0:
                    general_point_menu['submenu'] = []
                    for i in page_item.get_children():
                        if i.live and i.specific.show_main_menu:
                            general_point_menu['submenu'].append(
                                {
                                    'title': i.title,
                                    'url': i.url,
                                    'ordering': i.specific.ordering if hasattr(i.specific, 'ordering') else 10000
                                }
                            )

                    general_point_menu['submenu'].sort(key=lambda item: item['ordering'])
                main_menu.append(general_point_menu)
        main_menu.sort(key=lambda item: item['ordering'])
    return {
        'main_menu': main_menu
    }

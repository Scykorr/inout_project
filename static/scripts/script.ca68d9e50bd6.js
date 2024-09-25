const buttons = [...document.getElementsByClassName('review-readmore')]

let activeTab = 0
let activeTabEducation = 0
let activeTabEducationSecond = 0
let activeTabSearch = 0
let circlesCounter = 0

const stickyParent = document.getElementById('sticky-container')
const tabLeftItems = [...document.getElementsByClassName('features-tableft-item')]
const tableftSlides = document.getElementById('features-tableft-slides')

const theme = localStorage.getItem('theme')
if (document.getElementsByClassName('theme-switcher')[0]) {
    if (theme) {
        if (theme === 'dark') document.querySelector('html').classList.add('dark')
        else document.querySelector('html').classList.remove('dark')
    }

}

window.onload = () => {
    // setTimeout(function () {
    //     const preloader = document.getElementById('loader_start');
    //     if (!preloader.classList.contains('hidden')) {
    //         preloader.classList.add('hidden');
    //     }
    // }, 500)
    const stickyContainer = document.getElementById('sticky-container')
    const stickyBlock = document.getElementById('sticky-block')
    if (stickyContainer && stickyBlock) {
        if (window.innerHeight > 1200) {
            stickyContainer.classList.add('flex', 'justify-between')
            stickyBlock.classList.add('h-dvh', 'flex', 'flex-col', 'justify-center', 'sticky', 'top-0')
            stickyBlock.children[1].classList.add('flex', 'items-center')
        } else {
            stickyContainer.classList.add('justify-end')
            stickyBlock.classList.add('flex', 'flex-col', 'sticky', 'bottom-[100px]')
        }
    }
}

if (stickyParent) {
    window.addEventListener('scroll', () => {
        const onToggle = (index, percent) => {
            tabLeftItems.forEach((item, i) => {
                if (index === i) {
                    tableftSlides.children[i].classList.add('is-active')
                    item.classList.add('is-active')
                    item.children[0].children[0].style.height = `${percent}%`
                } else {
                    item.classList.remove('is-active')
                    tableftSlides.children[i].classList.remove('is-active')
                }
            })
        }

        const parentTop = stickyParent.getBoundingClientRect().top - 250
        const scrollPosition = Math.abs(parentTop)
        const totalHeight = 6000 - window.innerHeight
        const step = totalHeight / 5
        if (scrollPosition > 0 && scrollPosition < step) {
            onToggle(0, (100 / step) * scrollPosition)
        }
        if (scrollPosition > step && scrollPosition < step * 2) {
            onToggle(1, (100 / step) * scrollPosition - 100)
        }
        if (scrollPosition > step * 2 && scrollPosition < step * 3) {
            onToggle(2, (100 / step) * scrollPosition - 200)
        }
        if (scrollPosition > step * 3 && scrollPosition < step * 4) {
            onToggle(3, (100 / step) * scrollPosition - 300)
        }
        if (scrollPosition > step * 4 && scrollPosition < step * 5) {
            onToggle(4, (100 / step) * scrollPosition - 400)
        }
    })
}

if (buttons.length)
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            button.classList.toggle('hidden')
            button.parentElement.parentElement.children[0].classList.toggle('line-clamp-5')
            button.parentElement.parentElement.children[0].classList.toggle('line-clamp-5')
            button.parentElement.parentElement.children[3].classList.toggle('line-clamp-5')
        })
    })

const menu_items = document.querySelectorAll('.menu-item')
const category = document.querySelector('.category')
const heading = document.querySelector('.heading')

if (heading) {
    if (heading.textContent.length > 21) {
        heading.parentElement.classList.add('items-start')
        heading.parentElement.classList.remove('items-center')
    }
}

const toggleMenuImageActive = menu_item => {
    const is_dark = document.querySelector('html').classList.contains('dark')
    const is_clicked = menu_item.parentElement.dataset.clicked === 'true'

    if (!is_clicked) {
        if (is_dark) {
            const img = menu_item.querySelector('.dark')
            const img_active = menu_item.querySelector('.dark-active')

            img.classList.remove('dark:block')
            img.classList.add('dark:hidden')
            img_active.classList.remove('dark:hidden')
            img_active.classList.add('dark:block')
        } else {
            const img = menu_item.querySelector('.primary')
            const img_active = menu_item.querySelector('.primary-active')

            img.classList.add('hidden')
            img_active.classList.remove('hidden')
        }
    }
}

const toggleMenuImage = menu_item => {
    const is_dark = document.querySelector('html').classList.contains('dark')
    const is_clicked = menu_item.parentElement.dataset.clicked === 'true'

    if (!is_clicked) {
        if (is_dark) {
            const img = menu_item.querySelector('.dark')
            const img_active = menu_item.querySelector('.dark-active')

            img.classList.add('dark:block')
            img.classList.remove('dark:hidden')
            img_active.classList.add('dark:hidden')
            img_active.classList.remove('dark:block')
        } else {
            const img = menu_item.querySelector('.primary')
            const img_active = menu_item.querySelector('.primary-active')

            img.classList.remove('hidden')
            img_active.classList.add('hidden')
        }
    }
}

if (menu_items.length)
    menu_items.forEach(menu_item => {
        menu_item.addEventListener('mouseover', () => {
            toggleMenuImageActive(menu_item)
        })
    })

if (menu_items.length)
    menu_items.forEach(menu_item => {
        menu_item.addEventListener('mouseout', () => {
            toggleMenuImage(menu_item)
        })
    })

if (menu_items.length)
    menu_items.forEach(menu_item => {
        menu_item.addEventListener('click', () => {
            menu_item.parentElement.querySelector('.menu-list').classList.toggle('hidden')
            const is_clicked = menu_item.parentElement.dataset.clicked === 'true'
            const is_dark = document.querySelector('html').classList.contains('dark')
            const menu_item_text = menu_item.querySelector('p').textContent.trim()
            let is_selected = false
            if (category) {
                is_selected = category.textContent.trim() === menu_item_text
            }

            if (is_clicked && !is_selected) {
                menu_item.parentElement.dataset.clicked = 'false'

                if (is_dark) {
                    menu_item.classList.remove('dark:text-dark-text-primary')
                } else {
                    menu_item.classList.remove('text-text-primary')
                }
            } else {
                menu_item.parentElement.dataset.clicked = 'true'

                if (is_dark) {
                    menu_item.classList.add('dark:text-dark-text-primary')
                } else {
                    menu_item.classList.add('text-text-primary')
                }
            }
        })
    })

const theme_switcher = document.querySelector('.theme-switcher')
const theme_controls = theme_switcher ? theme_switcher.querySelectorAll('.theme-control') : null

if (theme_switcher) {
    theme_controls.forEach(theme_control => {
        theme_control.addEventListener('click', e => {
            const target = e.currentTarget
            if (target.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark')
                document.querySelector('html').classList.add('dark')
            } else {
                localStorage.setItem('theme', 'light')
                document.querySelector('html').classList.remove('dark')
            }
            // if (target.classList.contains('dark-theme')) {
            //   document.querySelector('html').classList.add('dark')
            // } else {
            //   document.querySelector('html').classList.remove('dark')
            // }
        })
    })
}

const search_wrapper = document.querySelector('.search-wrapper')
const search = search_wrapper ? search_wrapper.querySelector('.search') : null
const search_state = {is_focus: false}

if (search_wrapper) {
    search_wrapper.addEventListener('mouseover', () => {
        const is_dark = document.querySelector('html').classList.contains('dark')

        if (!search_state.is_focus) {
            if (is_dark) {
                const search_img = search_wrapper.querySelector('.search-img-dark')
                const search_img_active = search_wrapper.querySelector('.search-img-dark-active')

                search_img.classList.add('dark:hidden')
                search_img_active.classList.remove('dark:hidden')
                search_img_active.classList.add('dark:block')
            } else {
                const search_img = search_wrapper.querySelector('.search-img-primary')
                const search_img_active = search_wrapper.querySelector('.search-img-primary-active')

                search_img.classList.add('hidden')
                search_img_active.classList.remove('hidden')
            }
        }
    })
}

if (search_wrapper) {
    search_wrapper.addEventListener('mouseout', () => {
        const is_dark = document.querySelector('html').classList.contains('dark')

        if (!search_state.is_focus) {
            if (is_dark) {
                const search_img = search_wrapper.querySelector('.search-img-dark')
                const search_img_active = search_wrapper.querySelector('.search-img-dark-active')

                search_img.classList.remove('dark:hidden')
                search_img_active.classList.add('dark:hidden')
                search_img_active.classList.remove('dark:block')
            } else {
                const search_img = search_wrapper.querySelector('.search-img-primary')
                const search_img_active = search_wrapper.querySelector('.search-img-primary-active')

                search_img.classList.remove('hidden')
                search_img_active.classList.add('hidden')
            }
        }
    })
}

if (search_wrapper) {
    search_wrapper.addEventListener('click', () => {
        search.focus()
    })
}

if (search_wrapper) {
    search.addEventListener('focus', () => {
        const is_dark = document.querySelector('html').classList.contains('dark')
        search_state.is_focus = true

        if (is_dark) {
            const search_img = search_wrapper.querySelector('.search-img-dark')
            const search_img_active = search_wrapper.querySelector('.search-img-dark-active')

            search_img.classList.add('dark:hidden')
            search_img_active.classList.remove('dark:hidden')
            search_img_active.classList.add('dark:block')
            search_wrapper.classList.add('dark:border-[#ffffff]')
        } else {
            const search_img = search_wrapper.querySelector('.search-img-primary')
            const search_img_active = search_wrapper.querySelector('.search-img-primary-active')

            search_img.classList.add('hidden')
            search_img_active.classList.remove('hidden')
            search_wrapper.classList.add('border-[#000000]')
        }
    })
}

if (search_wrapper) {
    search.addEventListener('blur', () => {
        const is_dark = document.querySelector('html').classList.contains('dark')
        search_state.is_focus = false

        if (is_dark) {
            const search_img = search_wrapper.querySelector('.search-img-dark')
            const search_img_active = search_wrapper.querySelector('.search-img-dark-active')

            search_img.classList.remove('dark:hidden')
            search_img_active.classList.add('dark:hidden')
            search_img_active.classList.remove('dark:block')
            search_wrapper.classList.remove('dark:border-[#ffffff]')
        } else {
            const search_img = search_wrapper.querySelector('.search-img-primary')
            const search_img_active = search_wrapper.querySelector('.search-img-primary-active')

            search_img.classList.remove('hidden')
            search_img_active.classList.add('hidden')
            search_wrapper.classList.remove('border-[#000000]')
        }
    })
}

const articles_list = document.querySelector('.articles-list')

if (articles_list) {
    const length = articles_list.children.length

    if (length % 2 === 0) {
        articles_list.classList.add('[&_li:nth-last-child(-n+2)>div]:hidden')
    } else {
        articles_list.classList.add('[&_li:nth-last-child(1)>div]:hidden')
    }
}

const button = [...document.getElementsByClassName('features-typical-readmore')]

if (button.length)
    button.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.children[1].classList.toggle('hidden')
            button.children[0].classList.toggle('rotate-180')
        })
    })

// обработчики для input и wrapper project_management_news
const project_management_news_input = document.querySelector('.project_management_news_input')
const project_management_news_input_wrapper = document.querySelector('.project_management_news_input_wrapper')
const is_dark_theme = document.querySelector('html').classList.contains('dark')

if (project_management_news_input) {
    project_management_news_input.addEventListener('focus', () => {
        if (is_dark_theme) {
            project_management_news_input_wrapper.classList.remove('dark:border-[rgba(255,255,255,0.08)]')
            project_management_news_input_wrapper.classList.add('border-[#FFFFFF]')
        } else {
            project_management_news_input_wrapper.classList.remove('border-[rgba(0,0,0,0.08)]')
            project_management_news_input_wrapper.classList.add('border-[#000000]')
        }
    })
}

if (project_management_news_input) {
    project_management_news_input.addEventListener('blur', () => {
        if (is_dark_theme) {
            project_management_news_input_wrapper.classList.add('dark:border-[rgba(255,255,255,0.08)]')
            project_management_news_input_wrapper.classList.remove('border-[#FFFFFF]')
        } else {
            project_management_news_input_wrapper.classList.add('border-[rgba(0,0,0,0.08)]')
            project_management_news_input_wrapper.classList.remove('border-[#000000]')
        }
    })
}

if (project_management_news_input) {
    project_management_news_input_wrapper.addEventListener('click', () => {
        project_management_news_input.focus()
    })
}

if (project_management_news_input) {
    project_management_news_input_wrapper.addEventListener('mouseout', () => {
        const hover_mail_dark = project_management_news_input_wrapper.querySelector('.dark-hover')
        const mail_dark = project_management_news_input_wrapper.querySelector('.dark')
        const hover_mail_primary = project_management_news_input_wrapper.querySelector('.primary-hover')
        const mail_primary = project_management_news_input_wrapper.querySelector('.primary')

        if (is_dark_theme) {
            project_management_news_input.classList.remove('dark:placeholder:text-dark-text-primary')
            project_management_news_input.classList.add('dark:placeholder:text-dark-text-secondary')
            hover_mail_dark.classList.add('dark:hidden')
            hover_mail_dark.classList.remove('dark:block')
            mail_dark.classList.toggle('dark:hidden')
        } else {
            project_management_news_input.classList.remove('placeholder:text-text-primary')
            project_management_news_input.classList.add('placeholder:text-text-secondary')
            hover_mail_primary.classList.add('hidden')
            mail_primary.classList.remove('hidden')
        }
    })
}

if (project_management_news_input) {
    project_management_news_input_wrapper.addEventListener('mouseover', () => {
        const hover_mail_dark = project_management_news_input_wrapper.querySelector('.dark-hover')
        const mail_dark = project_management_news_input_wrapper.querySelector('.dark')
        const hover_mail_primary = project_management_news_input_wrapper.querySelector('.primary-hover')
        const mail_primary = project_management_news_input_wrapper.querySelector('.primary')

        if (is_dark_theme) {
            project_management_news_input.classList.add('dark:placeholder:text-dark-text-primary')
            project_management_news_input.classList.remove('dark:placeholder:text-dark-text-secondary')
            hover_mail_dark.classList.remove('dark:hidden')
            hover_mail_dark.classList.add('dark:block')
            mail_dark.classList.toggle('dark:hidden')
        } else {
            project_management_news_input.classList.add('placeholder:text-text-primary')
            project_management_news_input.classList.remove('placeholder:text-text-secondary')
            hover_mail_primary.classList.remove('hidden')
            mail_primary.classList.add('hidden')
        }
    })
}

const button_footer = [...document.getElementsByClassName('footer-readmore')]
if (button_footer.length)
    button_footer.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.children[2].classList.toggle('max-md:hidden')
            button.children[0].classList.toggle('rotate-180')
        })
    })

const technical_information_items = document.querySelectorAll('.technical-information-item')
if (technical_information_items.length)
    technical_information_items.forEach(item => {
        item.addEventListener('click', () => {
            const minus = item.querySelector('.minus')
            const plus = item.querySelector('.plus')
            const container = item.querySelector('.container')

            minus.classList.toggle('hidden')
            plus.classList.toggle('hidden')
            container.classList.toggle('hidden')
        })
    })

const pagination_items = document.querySelectorAll('.pagination-item')
let current_item = pagination_items[0]

if (pagination_items.length)
    pagination_items.forEach(item => {
        item.addEventListener('click', () => {
            if (current_item) {
                current_item.classList.remove(
                    'dark:text-dark-text-primary',
                    'text-text-primary',
                    'dark:bg-dark-card-and-Sec-BT',
                    'bg-card-and-Sec-BT'
                )
                current_item.classList.add('text-text-secondary', 'dark:text-dark-text-secondary')
                item.classList.remove('text-text-secondary', 'dark:text-dark-text-secondary')
                item.classList.add(
                    'dark:text-dark-text-primary',
                    'text-text-primary',
                    'dark:bg-dark-card-and-Sec-BT',
                    'bg-card-and-Sec-BT'
                )
                current_item = item
            }
        })
    })

const blog_nav_links = document.querySelectorAll('.nav-link')
let current_link = blog_nav_links[0]

if (blog_nav_links.length)
    blog_nav_links.forEach(item => {
        item.addEventListener('click', () => {
            if (current_link) {
                current_link.classList.remove('text-text-primary', 'dark:text-dark-text-primary', 'border-b')
                current_link.classList.add('text-text-tertiary', 'dark:text-dark-text-tertiary')
                item.classList.remove('text-text-tertiary', 'dark:text-dark-text-tertiary')
                item.classList.add('text-text-primary', 'dark:text-dark-text-primary', 'border-b')
                current_link = item
            }
        })
    })

const prices_switchers = document.querySelectorAll('.prices-switcher')
let current_switcher = prices_switchers[0]

if (prices_switchers.length)
    prices_switchers.forEach(switcher => {
        switcher.addEventListener('click', () => {
            if (current_switcher) {
                current_switcher.classList.remove('bg-card-and-Sec-BT', 'dark:bg-dark-card-and-Sec-BT')
                current_switcher.classList.add('text-text-secondary', 'dark:text-dark-text-secondary')
                switcher.classList.remove('text-text-secondary', 'dark:text-dark-text-secondary')
                switcher.classList.add('bg-card-and-Sec-BT', 'dark:bg-dark-card-and-Sec-BT')
                current_switcher = switcher
            }
        })
    })

const info_items = document.querySelectorAll('.info')
if (info_items.length)
    info_items.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.parentElement.querySelector('div').classList.remove('hidden')
        })
    })

if (info_items.length)
    info_items.forEach(item => {
        item.addEventListener('mouseout', () => {
            item.parentElement.querySelector('div').classList.add('hidden')
        })
    })

const prices_more_switcher = document.querySelector('.prices-more-switcher')
const prices_more_info = document.querySelector('.prices-more-info')
if (prices_more_switcher) {
    prices_more_switcher.addEventListener('click', () => {
        const prices_images = document.querySelectorAll('.prices-more-image')
        const is_clicked = prices_more_switcher.dataset.clicked === 'true'

        if (is_clicked) {
            prices_images.forEach(image => {
                image.classList.remove('rotate-180')
            })
            prices_more_switcher.dataset.clicked = 'false'
            prices_more_info.classList.toggle('hidden')
        } else {
            prices_images.forEach(image => {
                image.classList.add('rotate-180')
            })
            prices_more_switcher.dataset.clicked = 'true'
            prices_more_info.classList.toggle('hidden')
        }
    })
}

const blog_filters = document.querySelectorAll('.toggle-link')
const filter_item = document.querySelector('.filter-item')
const filter_menu = document.querySelector('.filter-menu')
const filter_item_images = document.querySelectorAll('.filter-item-image')
let current_filter = blog_filters[0]

if (filter_item) {
    filter_item.addEventListener('click', () => {
        if (filter_item.dataset.clicked === 'false') {
            filter_item_images.forEach(item_image => {
                filter_item.dataset.clicked = 'true'
                item_image.classList.add('rotate-180')
                filter_menu.classList.remove('hidden')
                filter_menu.classList.add('flex', 'flex-col')
            })
        } else {
            filter_item_images.forEach(item_image => {
                filter_item.dataset.clicked = 'false'
                item_image.classList.remove('rotate-180')
                filter_menu.classList.add('hidden')
                filter_menu.classList.remove('flex', 'flex-col')
            })
        }
    })
}

if (blog_filters.length)
    blog_filters.forEach(item => {
        item.addEventListener('click', () => {
            if (current_filter) {
                current_filter.classList.remove('dark:text-dark-text-link', 'text-text-link')
                current_filter.classList.add('text-text-primary', 'dark:text-dark-text-primary')
                item.classList.remove('text-text-primary', 'dark:text-dark-text-primary')
                item.classList.add('dark:text-dark-text-link', 'text-text-link')
                current_filter = item
                filter_item.children[0].textContent = item.textContent
            }
        })
    })

const mobileNav = document.getElementById('mobile-nav')
const burger = document.getElementById('burger')

if (burger)
    burger.addEventListener('click', () => {
        mobileNav.classList.toggle('translate-x-full')
        mobileNav.classList.toggle('translate-x-0')
    })

const button_header = [...document.getElementsByClassName('header-readmore')]
if (button_header.length)
    button_header.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.children[2].classList.toggle('max-md:hidden')
            button.children[0].classList.toggle('rotate-180')
        })
    })

let tabs = document.querySelectorAll('.tabheader__item'),
    tabsContent = document.querySelectorAll('.tabcontent'),
    tabsParent = document.querySelector('.tabheader__items'),
    tabheaderPrev = document.querySelector('.tabheader-pagination-prev'),
    tabheaderNext = document.querySelector('.tabheader-pagination-next')

function hideTabContent() {
    tabsContent.forEach(item => {
        item.classList.add('hidden')
        item.classList.remove('flex')
    })

    tabs.forEach(item => {
        item.classList.remove('dark:bg-dark-card-and-Sec-BT', 'bg-sec-BT', 'rounded-[8px]')
        item.classList.add('dark:text-dark-text-tertiary', 'text-text-tertiary')
    })
}

function showTabContent(i = 0) {
    tabsContent[i].classList.add('flex')
    tabsContent[i].classList.remove('hidden')
    tabs[i].classList.add('dark:bg-dark-card-and-Sec-BT', 'bg-sec-BT', 'rounded-[8px]')
    tabs[i].classList.remove('dark:text-dark-text-tertiary', 'text-text-tertiary')
    activeTab = i
    if (activeTab === 0) {
        tabheaderPrev.classList.add('hidden')
    } else if (activeTab === tabs.length - 1) {
        tabheaderNext.classList.add('hidden')
    } else {
        tabheaderPrev.classList.remove('hidden')
        tabheaderNext.classList.remove('hidden')
    }
}

if (tabsContent.length) hideTabContent()
if (tabs.length) showTabContent()

if (tabsParent)
    tabsParent.addEventListener('click', event => {
        const target = event.target
        if (target && target.classList.contains('tabheader__item')) {
            tabs.forEach((item, i) => {
                if (target === item) {
                    hideTabContent()
                    showTabContent(i)
                }
            })
        }
    })

if (tabheaderPrev)
    tabheaderPrev.addEventListener('click', () => {
        tabs[activeTab - 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTab > 0) {
            hideTabContent()
            showTabContent(activeTab - 1)
        }
    })

if (tabheaderNext)
    tabheaderNext.addEventListener('click', () => {
        tabs[activeTab + 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTab < tabs.length - 1) {
            hideTabContent()
            showTabContent(activeTab + 1)
        }
    })

let tabsElement = document.querySelectorAll('.tabheader__item_education'),
    tabsParentElements = document.querySelector('.tabheader__items_education'),
    tabsElementSecond = document.querySelectorAll('.tabheader__item_education-second'),
    tabsParentElementsSecond = document.querySelector('.tabheader__items_education-second'),
    tabheaderPrevEducation = document.querySelector('.tabheader-pagination-prev-education'),
    tabheaderNextEducation = document.querySelector('.tabheader-pagination-next-education'),
    tabheaderPrevEducationSecond = document.querySelector('.tabheader-pagination-prev-education-second'),
    tabheaderNextEducationSecond = document.querySelector('.tabheader-pagination-next-education-second')

function hideTabContentEducation() {
    tabsElement.forEach(item => {
        item.classList.add('colors-text-secondary', 'max-md:text-text-tertiary', 'dark:max-md:text-dark-text-tertiary')
        item.classList.remove('dark:max-md:bg-dark-card-and-Sec-BT', 'max-md:bg-sec-BT')
    })
}

function showTabContentEducation(i = 0) {
    tabsElement[i].classList.remove(
        'colors-text-secondary',
        'max-md:text-text-tertiary',
        'dark:max-md:text-dark-text-tertiary'
    )
    tabsElement[i].classList.add('dark:max-md:bg-dark-card-and-Sec-BT', 'max-md:bg-sec-BT')
    activeTabEducation = i
    if (activeTabEducation === 0) {
        tabheaderPrevEducation.classList.add('hidden')
    } else if (activeTabEducation === tabsElement.length - 1) {
        tabheaderNextEducation.classList.add('hidden')
    } else {
        tabheaderPrevEducation.classList.remove('hidden')
        tabheaderNextEducation.classList.remove('hidden')
    }
}

if (tabsElement.length) hideTabContentEducation()
if (tabsElement.length) showTabContentEducation()

if (tabsParentElements)
    tabsParentElements.addEventListener('click', event => {
        const target = event.target
        if (target && target.classList.contains('tabheader__item_education')) {
            tabsElement.forEach((item, i) => {
                if (target === item) {
                    hideTabContentEducation()
                    showTabContentEducation(i)
                }
            })
        }
    })

if (tabheaderPrevEducation)
    tabheaderPrevEducation.addEventListener('click', () => {
        tabsElement[activeTabEducation - 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTabEducation > 0) {
            hideTabContentEducation()
            showTabContentEducation(activeTabEducation - 1)
        }
    })

if (tabheaderNextEducation)
    tabheaderNextEducation.addEventListener('click', () => {
        tabsElement[activeTabEducation + 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTabEducation < tabsElement.length - 1) {
            hideTabContentEducation()
            showTabContentEducation(activeTabEducation + 1)
        }
    })

function hideTabContentEducationSecond() {
    tabsElementSecond.forEach(item => {
        item.classList.add('colors-text-tertiary')
        item.classList.remove('border-b-primary-bg', 'border-b-[1px]')
    })
}

function showTabContentEducationSecond(i = 0) {
    tabsElementSecond[i].classList.remove('colors-text-tertiary')
    tabsElementSecond[i].classList.add('border-b-primary-bg', 'border-b-[1px]')
    activeTabEducationSecond = i
    if (activeTabEducationSecond === 0) {
        tabheaderPrevEducationSecond.classList.add('hidden')
    } else if (activeTabEducationSecond === tabsElementSecond.length - 1) {
        tabheaderNextEducationSecond.classList.add('hidden')
    } else {
        tabheaderPrevEducationSecond.classList.remove('hidden')
        tabheaderNextEducationSecond.classList.remove('hidden')
    }
}

if (tabsElementSecond.length) hideTabContentEducationSecond()
if (tabsElementSecond.length) showTabContentEducationSecond()

if (tabsParentElementsSecond)
    tabsParentElementsSecond.addEventListener('click', event => {
        const target = event.target
        if (target && target.classList.contains('tabheader__item_education-second')) {
            tabsElementSecond.forEach((item, i) => {
                if (target === item) {
                    hideTabContentEducationSecond()
                    showTabContentEducationSecond(i)
                }
            })
        }
    })

if (tabheaderPrevEducationSecond)
    tabheaderPrevEducationSecond.addEventListener('click', () => {
        tabsElementSecond[activeTabEducationSecond - 1].scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'center',
        })
        if (activeTabEducationSecond > 0) {
            hideTabContentEducationSecond()
            showTabContentEducationSecond(activeTabEducationSecond - 1)
        }
    })

if (tabheaderNextEducationSecond)
    tabheaderNextEducationSecond.addEventListener('click', () => {
        tabsElementSecond[activeTabEducationSecond + 1].scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'center',
        })
        if (activeTabEducationSecond < tabsElementSecond.length - 1) {
            hideTabContentEducationSecond()
            showTabContentEducationSecond(activeTabEducationSecond + 1)
        }
    })
const faqItems = document.querySelectorAll('.faq-item')

if (faqItems.length)
    faqItems.forEach(item => {
        const plusIcon = item.querySelector('.plus')
        const minusIcon = item.querySelector('.minus')
        const answerBlock = item.querySelector('.faq-description')

        item.addEventListener('click', () => {
            answerBlock.classList.toggle('hidden')
            plusIcon.classList.toggle('hidden')
            minusIcon.classList.toggle('hidden')
        })
    })

const themeToggle = document.getElementById('themeToggle')
const moonIconLight = document.querySelector('.moonIconLight')
const moonIconDark = document.querySelector('.moonIconDark')
const sunIconLight = document.querySelector('.sunIconLight')
const sunIconDark = document.querySelector('.sunIconDark')

if (themeToggle) {
    themeToggle.addEventListener('click', function () {
        document.documentElement.classList.toggle('dark')
        moonIconLight.classList.toggle('hidden')
        moonIconDark.classList.toggle('hidden')
        sunIconLight.classList.toggle('hidden')
        sunIconDark.classList.toggle('hidden')
    })
}

document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.breadcrumbs_link a')

    links.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault()

            links.forEach(function (item) {
                item.classList.remove('dark-base-text-accent', 'dark:dark-base-text-accent', 'font-normal')
                item.parentElement.classList.add('text-text-secondary', 'dark:text-dark-text-secondary')
                item.parentElement.classList.remove('border-b')
            })

            link.parentElement.classList.remove('text-text-secondary', 'dark:text-dark-text-secondary')
            link.parentElement.classList.add('dark-base-text-accent', 'dark:dark-base-text-accent', 'font-normal')
            link.parentElement.classList.add('border-b')
        })
    })
})

document.addEventListener('DOMContentLoaded', function () {
    const toggleLinks = document.querySelectorAll('.toggle-link')

    toggleLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault()

            const text = link.textContent.trim()

            const parentElement = link.closest('.relative')

            const spanElement = parentElement.querySelector('span')

            spanElement.textContent = text
        })
    })
})

document.addEventListener('DOMContentLoaded', function () {
    const logo = document.getElementById('logo')
    const tryButton = document.getElementById('tryButton')
    const burger = document.getElementById('burger')
    const input = document.getElementById('input')
    const searchIcon = document.getElementById('searchIcon')
    const searchInputContainer = document.getElementById('searchInputContainer')
    const cancelSearch = document.getElementById('cancelSearch')

    if (searchIcon) {
        searchIcon.addEventListener('click', function (event) {
            event.preventDefault()
            logo.classList.add('max-sm:hidden')
            input.classList.add('max-sm:w-[88dvw]')
            tryButton.classList.add('max-sm:hidden')
            burger.classList.add('max-sm:hidden')
            searchIcon.classList.add('hidden')
            searchInputContainer.classList.remove('hidden')
        })
    }

    if (cancelSearch) {
        cancelSearch.addEventListener('click', function () {
            searchIcon.classList.remove('hidden')
            logo.classList.remove('max-sm:hidden')
            input.classList.remove('max-sm:w-[88dvw]')
            tryButton.classList.remove('max-sm:hidden')
            burger.classList.remove('max-sm:hidden')
            searchInputContainer.classList.add('hidden')
        })
    }
})

let tabsSearch = document.querySelectorAll('.tabheader__item_search'),
    tabsParentSearch = document.querySelector('.tabheader__items_search'),
    tabheaderPrevSearch = document.querySelector('.tabheader-pagination-prev-search'),
    tabheaderNextSearch = document.querySelector('.tabheader-pagination-next-search')

function hideTabContentSearch() {
    tabsSearch.forEach(item => {
        item.classList.add('colors-text-tertiary')
        item.classList.remove('border-b-primary-bg', 'border-b-[1px]')
    })
}

function showTabContentSearch(i = 0) {
    tabsSearch[i].classList.remove('colors-text-tertiary')
    tabsSearch[i].classList.add('border-b-primary-bg', 'border-b-[1px]')
    activeTabSearch = i
    if (activeTabSearch === 0) {
        tabheaderPrevSearch.classList.add('hidden')
    } else if (activeTabSearch === tabsSearch.length - 1) {
        tabheaderNextSearch.classList.add('hidden')
    } else {
        tabheaderPrevSearch.classList.remove('hidden')
        tabheaderNextSearch.classList.remove('hidden')
    }
}

if (tabsSearch.length) hideTabContentSearch()
if (tabsSearch.length) showTabContentSearch()

if (tabsParentSearch)
    tabsParentSearch.addEventListener('click', event => {
        const target = event.target
        if (target && target.classList.contains('tabheader__item_search')) {
            tabsSearch.forEach((item, i) => {
                if (target === item) {
                    hideTabContentSearch()
                    showTabContentSearch(i)
                }
            })
        }
    })

if (tabheaderPrevSearch)
    tabheaderPrevSearch.addEventListener('click', () => {
        tabsSearch[activeTabSearch - 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTabSearch > 0) {
            hideTabContentSearch()
            showTabContentSearch(activeTabSearch - 1)
        }
    })

if (tabheaderNextSearch)
    tabheaderNextSearch.addEventListener('click', () => {
        tabsSearch[activeTabSearch + 1].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})
        if (activeTabSearch < tabsSearch.length - 1) {
            hideTabContentSearch()
            showTabContentSearch(activeTabSearch + 1)
        }
    })

const inputSearch = document.getElementById('inputSearch')
const clearButtonSearch = document.querySelector('.input-search-clear')

if (inputSearch)
    inputSearch.addEventListener('input', () => {
        if (inputSearch.value) {
            clearButtonSearch.classList.remove('hidden')
        } else {
            clearButtonSearch.classList.add('hidden')
        }
    })

if (clearButtonSearch)
    clearButtonSearch.addEventListener('click', () => {
        inputSearch.value = ''
        clearButtonSearch.classList.add('hidden')
    })

const buttonRequest = [...document.getElementsByClassName('request-form-readmore')]
let selectElementRequest = [...document.getElementsByClassName('select-element-request')]

if (selectElementRequest.length) {
    selectElementRequest.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.parentElement.children[0].textContent = button.textContent
            button.parentElement.parentElement.children[0].classList.remove('colors-text-secondary')
        })
    })
}

if (buttonRequest.length) document.addEventListener('click', e => {
    if (!buttonRequest[0].contains(e.target)) {
        buttonRequest.forEach(item => {
            item.children[3].classList.add('hidden')
            item.children[1].classList.remove('rotate-180')
            item.children[2].classList.remove('rotate-180')
        })
    }
})

if (buttonRequest.length) {
    buttonRequest.forEach(button => {
        button.addEventListener('click', () => {
            button.children[3].classList.toggle('hidden')
            button.children[1].classList.toggle('rotate-180')
            button.children[2].classList.toggle('rotate-180')
        })
    })
}

const buttonPRequest = [...document.getElementsByClassName('request-form-p-readmore')]
let selectPElementRequest = [...document.getElementsByClassName('select-element-p-request')]

if (selectPElementRequest.length) {
    selectPElementRequest.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.parentElement.children[0].textContent = button.textContent
            button.parentElement.parentElement.children[0].classList.remove('colors-text-secondary')
        })
    })
}

if (buttonPRequest.length) document.addEventListener('click', e => {
    if (!buttonPRequest[0].contains(e.target)) {
        buttonPRequest.forEach(item => {
            item.children[3].classList.add('hidden')
            item.children[1].classList.remove('rotate-180')
            item.children[2].classList.remove('rotate-180')
        })
    }
})

if (buttonPRequest.length) {
    buttonPRequest.forEach(button => {
        button.addEventListener('click', () => {
            button.children[3].classList.toggle('hidden')
            button.children[1].classList.toggle('rotate-180')
            button.children[2].classList.toggle('rotate-180')
        })
    })
}

let isDarkFavicon = document.querySelector('html').classList.contains('dark'),
    faviconSwapper = document.querySelector('link[rel="icon"]')
    faviconASwapper = document.querySelector('link[rel="apple-touch-icon"]')
    faviconMSwapper = document.querySelector('link[rel="mask-icon"]')

function swapFavicon() {
    if (isDarkFavicon) {
        faviconSwapper.setAttribute('href', '/static/icons/logos/favicon_dark.ico');
        faviconASwapper.setAttribute('href', '/static/icons/logos/favicon_dark.png');
        faviconMSwapper.setAttribute('href', '/static/icons/logos/favicon_dark.png');
    } else {
        faviconSwapper.setAttribute('href', '/static/icons/logos/favicon_light.ico');
        faviconASwapper.setAttribute('href', '/static/icons/logos/favicon_light.png');
        faviconMSwapper.setAttribute('href', '/static/icons/logos/favicon_light.png');
    }
}

swapFavicon();

const requestForm = document.getElementById('request_form')
const buttonsForOpenForm = document.querySelectorAll('[data-open-form]');
const closeForm = document.querySelector('[data-close-form]');
const closeFormMobile = document.querySelector('[data-close-form-mobile]');

if (requestForm && buttonsForOpenForm.length && closeForm) {
    closeForm.addEventListener('click', () => {
        requestForm.classList.add('hidden')
        return false
    })
    closeFormMobile.addEventListener('click', () => {
        requestForm.classList.add('hidden')
        return false
    })
    buttonsForOpenForm.forEach(button => {
        button.addEventListener('click', () => {
            if (requestForm.classList.contains('hidden')) {
                requestForm.classList.remove('hidden')
                return false
            } else {
                requestForm.classList.add('hidden')
                return false
            }
        })
    })
}

const requestPartnerForm = document.getElementById('request_partner_form')
const buttonsForOpenPartnerForm = document.querySelectorAll('[data-open-partner-form]');
const closePartnerForm = document.querySelector('[data-close-partner-form]');
const closePartnerFormMobile = document.querySelector('[data-close-form-partner-mobile]');
if (requestPartnerForm && buttonsForOpenPartnerForm.length && closePartnerForm) {
    closePartnerForm.addEventListener('click', () => {
        requestPartnerForm.classList.add('hidden')
    })
    closePartnerFormMobile.addEventListener('click', () => {
        requestPartnerForm.classList.add('hidden')
    })
    buttonsForOpenPartnerForm.forEach(button => {
        button.addEventListener('click', () => {
            if (requestPartnerForm.classList.contains('hidden')) {
                requestPartnerForm.classList.remove('hidden')
            } else {
                requestPartnerForm.classList.add('hidden')
            }
        })
    })
}

const circlesElement = document.querySelectorAll('.circles-element')

if (circlesElement.length) {
    setInterval(() => {
        circlesTransition(circlesCounter)
    }, 1000)
}

function circlesTransition(i) {
    circlesElement[i].children[0].classList.toggle('opacity-100')
    circlesElement[i].children[1].classList.toggle('opacity-100')
    setTimeout(() => {
        circlesElement[i].children[0].classList.toggle('opacity-100')
        circlesElement[i].children[1].classList.toggle('opacity-100')
    }, 1000)
    circlesCounter > 6 ? circlesCounter = 0 : circlesCounter++
}


const loader = document.getElementById('loader_form')
// Form handling

const formInputsForm = [...document.querySelectorAll('#request_form input')]

function checkForm(){
    const firstNameFilled = document.querySelector('#request_form input[name=firstname]').value.length > 0
    const lastNameFilled = document.querySelector('#request_form input[name=lastname]').value.length > 0
    const titleFilled = document.querySelector('#request_form #request-form-readmore span').textContent.length > 0
    const phoneFilled = document.querySelector('#request_form input[name=phone]').value.length > 0
    const emailFilled = document.querySelector('#request_form input[name=email]').value.length > 0
    const companyFilled = document.querySelector('#request_form input[name=company]').value.length > 0
    if (firstNameFilled && lastNameFilled && phoneFilled && emailFilled && companyFilled) {
        return true;
    }

    return false
}

formInputsForm.forEach((item, i) => {
    item.addEventListener('input', (e) => {
        if (checkForm()) {
            console.log('input')
            document.querySelector('#request_form button[name=send_form]').style.backgroundColor = 'white'
            document.querySelector('#request_form button[name=send_form_mobile]').style.backgroundColor = 'white'
        }
    })
})

const formInputsPartnerForm = [...document.querySelectorAll('#request_partner_form input')]

function checkPartnerForm() {
    const firstNameFilled = document.querySelector('#request_partner_form input[name=firstname]').value.length > 0
        const lastNameFilled = document.querySelector('#request_partner_form input[name=lastname]').value.length > 0
        // const titleFilled = document.querySelector('#request_partner_form #request-form-readmore span').textContent.length > 0
        const phoneFilled = document.querySelector('#request_partner_form input[name=phone]').value.length > 0
        const emailFilled = document.querySelector('#request_partner_form input[name=email]').value.length > 0
        const companyFilled = document.querySelector('#request_partner_form input[name=company]').value.length > 0

        if (firstNameFilled && lastNameFilled && phoneFilled && emailFilled && companyFilled) {
            return true;
        }
        return false;
}

formInputsPartnerForm.forEach((item, i) => {
    item.addEventListener('input', (e) => {
        if (checkPartnerForm()){
            document.querySelector('#request_partner_form button[name=send_form]').style.backgroundColor = 'white'
            document.querySelector('#request_partner_form button[name=send_form_mobile]').style.backgroundColor = 'white'
        }
    })
})

function getCSRF(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

 if (requestForm) {
     requestForm.addEventListener('submit', (e) => {
         e.preventDefault(); // before the code
         requestForm.classList.add('hidden')
         loader.classList.remove('hidden')
         var xhr = new XMLHttpRequest();
         xhr.open("POST", "/api/trial/", true);
         xhr.setRequestHeader('Content-Type', 'application/json');
         // xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
         xhr.send(JSON.stringify({
             custom_entity: {
                 external_values: {
                     client_firstname: document.querySelector('#request_form input[name=firstname]').value,
                     client_lastname: document.querySelector('#request_form input[name=lastname]').value,
                     client_position: document.querySelector('#request_form #request-form-readmore span').textContent,
                     client_phone: document.querySelector('#request_form input[name=phone]').value,
                     client_email: document.querySelector('#request_form input[name=email]').value,
                     company_name: document.querySelector('#request_form input[name=company]').value
                 }
             }
             //     #request-form-readmore span
         }));
         xhr.onreadystatechange = function () {
             if (this.readyState != 4) return;

             if (this.status == 200) {
                 // let newTab = window.open();
                 window.location.href = this.responseText;
                 // loader.classList.add('hidden')
             }
         };
         return false
     })
 }

 if (requestPartnerForm) {
// Form partner handling
     requestPartnerForm.addEventListener('submit', (e) => {
         e.preventDefault(); // before the code
         requestPartnerForm.classList.add('hidden')
         loader.classList.remove('hidden')
         var xhr = new XMLHttpRequest();
         xhr.open("POST", "/api/crm/", true);
         xhr.setRequestHeader('Content-Type', 'application/json');
         // xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
         xhr.send(JSON.stringify({
             easy_lead: {
                 first_name: document.querySelector('#request_partner_form input[name=firstname]').value,
                 last_name: document.querySelector('#request_partner_form input[name=lastname]').value,
                 job_title: document.querySelector('#request_partner_form #request-form-p-readmore span').textContent,
                 telephone: document.querySelector('#request_partner_form input[name=phone]').value,
                 mobile_phone: document.querySelector('#request_partner_form input[name=phone]').value,
                 email: document.querySelector('#request_partner_form input[name=email]').value,
                 company_name: document.querySelector('#request_partner_form input[name=company]').value,
                 value: '',
                 score: '',
                 source: '',
                 description: '',
                 country_code: "RU",
                 website: "http://www.example.com/",
                 disqualification_reason: "",
                 archived: false,
                 author_id: 113,
                 assigned_to_id: 1,
                 easy_campaign_id: 7,
                 easy_lead_status_id: 100,
                 easy_lead_priority_id: 126,
                 easy_lead_source_id: 119
             }
             //     #request-form-readmore span
         }));
         xhr.onreadystatechange = function () {
             if (this.readyState != 4) return;

             if (this.status == 200) {
                 loader.classList.add('hidden')
             }
         };
         return false
     })
 }

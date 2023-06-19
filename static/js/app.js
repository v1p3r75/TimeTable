const BASE_URL = 'http://localhost:8000/'

const PAGE_ATTR = 'timetable-page'


const App = {

    init: async function () {

        $('a[data-' + PAGE_ATTR + ']').each( (index, element) => {

            $(element).on('click', (e)  => {

                const target = e.target.nodeName == 'A' ? e.target : $(e.target).parents('a')
                const page = $(target).data(PAGE_ATTR)
                window.location.hash = page
            })

        });

    }(),

    preloader: function () {

        document.addEventListener('DOMContentLoaded', async (e) => {
            document.querySelector('.preloader').style.display = 'none';

            if(window.location.hash !== '') {
                const data = await App.fetch(BASE_URL + window.location.hash.slice(1)) 
                $('main').html(data)
            }
        })
    }(),

    loadPage: async function() {

        $(window).on('hashchange', async (e) => {

            const data = await App.fetch(BASE_URL + window.location.hash.slice(1))
            $('main').html(data)
        })
    }(),

    fetch: async function (url, options = {type: 'GET', data : null}) {

        let result = null

        await $.ajax({

            url,
            ...options,
            success: (response) => {
                result = response
            },
        });

        return result;
    }

}
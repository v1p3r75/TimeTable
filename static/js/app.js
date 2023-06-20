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

        $('.logout-btn').on('click', () => {

            App.alert('question', () => {
                window.location.href =  BASE_URL + '/auth/logout'
            })
        })

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
    },

    mobileSidebar: function () {

        const DISPLAY_CLASS = 'd-block position-abolute top-0 start-0'
        const HIDE_CLASS = 'col d-none d-lg-block col-lg-3'
        
        $('.bars-mobile').on('click', (e) => {

            $('.bars-mobile').children('i').removeClass('mdi-menu')

            $('.sidebar a[data-' + PAGE_ATTR + ']').each( (index, element) => {

                $(element).on('click', (e)  => {
    
                    $('.sidebar').removeClass(DISPLAY_CLASS)
                        .addClass(HIDE_CLASS)
                })
    
            });

            if($('.sidebar').hasClass('col')) {
                $('.sidebar').removeClass(HIDE_CLASS)
                .addClass(DISPLAY_CLASS)
            }else {
                $('.sidebar').addClass(HIDE_CLASS)
                .removeClass(DISPLAY_CLASS)
            }
        })
    }(),

    alert: (type, callback) => {

        if (type === 'question') {

            Swal.fire({
                title: 'Déconnexion',
                text: "Vous êtes sûr de vouloir vous deconnecter ?",
                showCancelButton: true,
                confirmButtonColor: '#3D5EE1',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Oui',
                cancelButtonText: 'Non',
              }).then((result) => {
                if (result.isConfirmed) {
                    return callback()
                //   Swal.fire(
                //     'Deleted!',
                //     'Your file has been deleted.',
                //     'success'
                //   )
                }
              })
        }
    }

}
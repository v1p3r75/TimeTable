$(document).ready(function() {

    const BASE_URL = '';

    const PAGE_ATTR = 'timetable-page';

    const langueOptions = {

        sEmptyTable: "Aucune donnée disponible dans le tableau",
        sInfo: "Affichage de _START_ à _END_ sur _TOTAL_ entrées",
        sInfoEmpty: "Affichage de 0 à 0 sur 0 entrée",
        sInfoFiltered: "(filtré à partir de _MAX_ entrées au total)",
        sInfoPostFix: "",
        sInfoThousands: ",",
        sLengthMenu: "Afficher _MENU_ entrées",
        sLoadingRecords: "Chargement...",
        sProcessing: "Traitement en cours...",
        sSearch: "Rechercher :",
        sZeroRecords: "Aucun résultat trouvé",
        oPaginate: {
            sFirst: "Premier",
            sLast: "Dernier",
            sNext: "Suivant",
            sPrevious: "Précédent"
        },
        oAria: {
            sSortAscending: ": activer pour trier la colonne par ordre croissant",
            sSortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    };

    const App = {

        init: async function() {
            
            window.langueOptions = langueOptions;


            $('a[data-' + PAGE_ATTR + ']').each((index, element) => {
                $(element).on('click', (e) => {
                    const target = e.target.nodeName == 'A' ? e.target : $(e.target).parents('a');
                    const page = $(target).data(PAGE_ATTR);
                    window.location.hash = page;
                });
            });

            $('.logout-btn').on('click', () => {
                App.alert('question', 'Déconnexion', 'Êtes-vous sûr de vouloir vous déconnecter ?', () => {
                    window.location.href = BASE_URL + '/auth/logout';
                });
            });

            $('.notify-icon').each((i, e) => {

                $(e).on('click', () => {
                    App.alert('info', 'Notification', 'Les notifications vous concernant sont envoyer directement sur votre boite mail. Merci !')
                })
            })

        }(),

        preloader: function() {
            
            $(document).ready(async function() {

                $('.preloader').hide();
                if (window.location.hash !== '') {

                    const data = await App.fetch(BASE_URL + window.location.hash.slice(1));
                    $('main').html(data);
                }else {

                    const data = await App.fetch(BASE_URL + $('.label-dashboard').data(PAGE_ATTR));
                    $('main').html(data);
                }
            });
        }(),

        loadPage: async function() {

            $(window).on('hashchange', async function() {
                const page = await App.fetch(BASE_URL + window.location.hash.slice(1));
                $('main').html(page);
            });
        }(),

        fetch: async function(url, options = { type: 'GET', data: null }) {
            let result = null;
            await $.ajax({
                url,
                ...options,
                success: function(response) {
                    result = response;
                },
            });
            return result;
        },

        toggleSidebar: function() {

            $('.bars-lg').on('click', () => {
                
                if ($('.sidebar').hasClass('col-lg-3')) {

                    $('.sidebar').removeClass('d-lg-block col-lg-3 animate__animated animate__fadeInLeft')
                    $('.logo').removeClass('d-lg-block col-lg-3 animate__animated animate__fadeInLeft')
                    $('.main').removeClass('col-lg-9')
                    $('.header-nav').removeClass('col-lg-9')

                }else {
                    
                    $('.sidebar').addClass('d-lg-block col-lg-3 animate__animated animate__fadeInLeft')
                    $('.logo').addClass('d-lg-block col-lg-3 animate__animated animate__fadeInLeft')
                    $('.main').addClass('col-lg-9')
                    $('.header-nav').addClass('col-lg-9')
                }
                
            })

        }(),

        mobileSidebar: function() {

            const DISPLAY_CLASS = 'd-block position-absolute top-0 start-0 animate__animated animate__fadeInLeft';
            const HIDE_CLASS = 'col d-none d-lg-block col-lg-3';

            $('.bars-mobile').on('click', function(e) {
                $('.bars-mobile').children('i').removeClass('mdi-menu');

                $('.sidebar a[data-' + PAGE_ATTR + ']').each(function(index, element) {
                    $(element).on('click', function(e) {
                        $('.sidebar')
                            .removeClass(DISPLAY_CLASS)
                            .addClass(HIDE_CLASS);
                    });
                });

                if ($('.sidebar').hasClass('col')) {
                    $('.sidebar')
                        .removeClass(HIDE_CLASS)
                        .addClass(DISPLAY_CLASS);
                } else {
                    $('.sidebar')
                        .addClass(HIDE_CLASS)
                        .removeClass(DISPLAY_CLASS);
                }
            });
        }(),

        alert: function(type, title, text, callback) {
            if (type === 'question') {
                Swal.fire({
                    title,
                    text,
                    showCancelButton: true,
                    confirmButtonColor: '#3D5EE1',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Oui',
                    cancelButtonText: 'Non',
                }).then((result) => {
                    if (result.isConfirmed) {
                        return callback();
                    }
                });
            }
            if (type === 'info') {

                Swal.fire({
                    title,
                    text,
                })
            }
        },

        getCookie: function (name) {
            
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            
            if (parts.length === 2) {
                return parts.pop().split(';').shift();
            }
            
            return null;
        }
    };

    window.App = App;
})
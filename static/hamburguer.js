//JavaScript feito para o botão dropdown estilo hamburguer - usado na navbar para telas menores

document.addEventListener("DOMContentLoaded", function() {
    var toggleButton = document.getElementById("navbarToggle");
    var navbarMenu = document.getElementById("navbarNav");

    function toggleMenu() { //funcao para alternar o menu da nav com base em atributos HTML usados - abrir ou fechar usando a logica de remover ou não a classe collapse
        if (navbarMenu.classList.contains("collapse")) {
            navbarMenu.classList.remove("collapse");
            toggleButton.setAttribute("aria-expanded", "true");  //o dropdown acontece
        } else {
            navbarMenu.classList.add("collapse");
            toggleButton.setAttribute("aria-expanded", "false");
        }
    }

    //atribuindo o event listener ao botão hamburguer para alternar o menu durante o click
    toggleButton.addEventListener("click", toggleMenu);

    //atribuindo o event listener a todos os links dentro da navbar para fechar o menu depois do click e redirecionar para as outras paginas caso necessario
    var navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    navLinks.forEach(function(link) { //uso de foreach para cada link
        link.addEventListener("click", function() {
            if (!navbarMenu.classList.contains("collapse")) {
                toggleMenu();  //chamada da funcao de alternancia do menu novamente - verificando a logica a ser seguida para os casos de estado do botão de menu (aberto ou fechado)
            }
        });
    });
});
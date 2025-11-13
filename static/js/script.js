// Sistema de Gestión de Tareas - JavaScript
console.log('Sistema de Tareas cargado correctamente');

document.addEventListener('DOMContentLoaded', function() {
    // Animación para los mensajes flash
    const flashMessages = document.querySelectorAll('.bg-red-100, .bg-green-100');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.transition = 'opacity 0.5s ease';
            message.style.opacity = '0';
            setTimeout(() => {
                if (message.parentElement) {
                    message.parentElement.removeChild(message);
                }
            }, 500);
        }, 3000);
    });

    // Confirmación para eliminar tareas
    const deleteButtons = document.querySelectorAll('a[href*="eliminar_tarea"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que quieres eliminar esta tarea?')) {
                e.preventDefault();
            }
        });
    });

    // Efecto hover en las tarjetas de tareas
    const taskCards = document.querySelectorAll('.bg-white.rounded-lg');
    taskCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
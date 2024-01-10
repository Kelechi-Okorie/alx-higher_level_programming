function handler () {
  $('div#add_item').click(() => {
    $('<li>Item</li>').append('ul.my_list');
  });

  $('div#remove_item').click(() => {
    $('.my_list li').last().remove();
  });

  $('div#clear_list').click(() => {
    $('.my_list li').map(() => {
      this.remove();
    });
  });
}

window.addEventListener('DOMContentLoaded', handler);

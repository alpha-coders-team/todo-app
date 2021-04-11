function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function completedTask(cb) {
    console.log(cb);
    console.log("Clicked, new value = " + cb.checked);
    console.log(cb.getAttribute("id").split('_')[1]);
    const id_item = cb.getAttribute("id").split('_')[1];
    $.ajax({
        url: cb.getAttribute("data-url"),
        type: 'delete',
        success: function (data) {
            console.log('was deleted');
            const item = document.querySelector('#task-item-'+id_item);
            console.log(item);
            item.remove();
        }
      });
  }
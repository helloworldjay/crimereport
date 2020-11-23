const input_commnet = (post_id) => {
    const sendData = new Object();
    str = $(this).create_comment.text();
    console.log(str, post_id)
    sendData.text = str
    sendData.post_id = post_id
    var jsonData = JSON.stringify(sendData)
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/post/postList/<int:post_id>/input_comment/",
        data: jsonData,
        dataType: "json",
        success: function (response) {
            $('.detail-container ul').append(
                "<li>" +
                    "<span class='reple-text'>" + response.text + "</span>" +
                    "<span class='reple-created'>" + response.created + "</span>" +
                "</li>"
            );
        }
    });
    }
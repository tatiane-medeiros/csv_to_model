    $("#id_dataset").change(function () {
        const url = $("#tipoForm").attr("data-sources-url");  // get the url of the `load_cities` view
        const myId = $(this).val();

        $.ajax({                       // initialize an AJAX request
            url: 'tabela/ajax/load-sources',                    // set the url of the request (= /persons/ajax/load-cities/ )

            success: function () {   // `data` is the return of the `load_cities` view function
                $("#id_source").html();  // replace the contents of the city input with the data that came from the server
                let html_data = '<option value="">selecione</option>';
                data.forEach(function (source) {
                    html_data += `<option value="${source.id}">${source.tipo}</option>`
                });
                console.log(html_data);
                $("#id_source").html(html_data);
            }
        });
    });
    document.getElementById('id_tipofonte').addEventListener('change', function() {
        this.form.submit();
    });
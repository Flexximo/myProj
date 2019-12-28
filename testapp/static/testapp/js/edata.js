//AJAX//

$("#number").change(function() {
    $("#number").removeAttr("value");
    $("#invoice_date").removeAttr("value");
    $("#supply_date").removeAttr("value");
    $("#comment").removeAttr("value");

    number = $("#number").val();


        $.ajax({
                type: "GET",
                url: "check_data_pk/",
                data: {
                    "number": number,
                },
                dataType: "text",
                cache: false,
                success: function(data) {
                    if(data == "ok") {
                        $("#number").css("color", "#66ff66");
                        $("#invoice_date").attr("placeholder", "Put invoice number");
                        $("#save_button").attr("disabled", false);
                        $("#save_button").css("background-color", "rgb(28, 100, 184)");
                    } else if (data == "no") {
                        $("#number").attr("placeholder", "Invoice name format, example: INV-000001");
                        $("#number").addClass("placeholder-pink");
                        $("#number").css("color", "red");
                        $("#save_button").attr("disabled", true);
                        $("#save_button").css("background-color", "red")
                    } else if(data == "already exists") {
                        $("#number").css("color", "red");
                        alert("This invoice number already exists");
                        $("#save_button").attr("disabled", true);

                    }
                }
        });

})

$("#invoice_date").change(function (){

    invoice_date = $("#invoice_date").val();



        $.ajax({
                type: "GET",
                url: "check_data_pk/",
                data: {
                    "invoice_date": invoice_date,
                },
                dataType: "text",
                cache: false,
                success: function(data) {
                    if(data == "ok") {
                        $("#invoice_date").css("color", "#66ff66");
                        $("#invoice_date").attr("placeholder", "Choose date");
                    } else if (data == "no"){
                        $("#invoice_date").attr("placeholder", "Use correct date format");
                        $("#invoice_date").addClass("placeholder-pink");
                        $("#invoice_date").css("color", "red");
                    }
                }

        });

})

$("#supply_date").change(function () {

    supply_date = $("#supply_date").val();
       $.ajax({
                type: "GET",
                url: "check_data_pk/",
                data: {
                    "supply_date": supply_date,
                },
                dataType: "text",
                cache: false,
                success: function(data) {
                    if(data == "ok") {
                        $("#supply_date").css("color", "#66ff66");
                        $("#supply_date").attr("placeholder", "Choose date");
                    } else if (data == "no"){
                        $("#supply_date").attr("placeholder", "Use correct date format");
                        $("#supply_date").addClass("placeholder-pink");
                        $("#save_button").attr("disabled", true);
                    }
                }
        });

})

$("#comment").change(function () {

    comment = $("#comment").val();



        $.ajax({
                type: "GET",
                url: "check_data_pk/",
                data: {
                    "comment": comment,
                },
                dataType: "text",
                cache: false,
                success: function(data) {
                    if(data == "ok") {
                        $("#comment").css("color", "#66ff66");
                        $("#comment").attr("placeholder", "Leave a comment");

                    } else if (data == "no") {
                        $("#comment").css("color", "red");
                        $("#comment").attr("placeholder", "Scripting symbols not allowed");
                        $("#comment").addClass("placeholder-pink");
                        $("#save_button").attr("disabled", true);
                    }
                }
        });
})







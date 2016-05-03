var API_KEY = "";

function getForecast(lat, lon) {
    var paramsString = $.param({"units": "si"});
    var url = "https://api.forecast.io/forecast/" + API_KEY + "/" + lat + "," + lon + "?" + paramsString;
    $.ajax(url, {
        success: function (data) {},
        error : function () {}
    });
}

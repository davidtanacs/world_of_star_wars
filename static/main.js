$(document).ready(function() {
    $("[id=resident]").click(function() {
        var $row = $(this).closest("tr"),        // Finds the closest row <tr> 
    $tds = $row.find("td:nth-child(1)"); // Finds the 1st <td> element
    $.each($tds, function() {                // Visits every single <td> element
    var planetName = $(this).text();         // Prints out the text within the <td>
    var pageNum = document.getElementById("page_num").value;
    $.getJSON('https://swapi.co/api/planets/?page=' + pageNum, function(response) {
    var planetsDatas = response['results'];
    for (var i = 0; i < planetsDatas.length; i ++) {
        if (planetName.includes(planetsDatas[i]['name'])) {
            var residentsLinks = (planetsDatas[i]['residents']);
        }
       };
       var residentsDatas = [];
    for (var i = 0; i < residentsLinks.length; i++) {
        $.getJSON(residentsLinks[i], function(residents) {
            var table = document.getElementById("residentsModal");
            var row = table.insertRow(0);
            var propertyList = ["name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_color", "gender"]
            for (var j = 0; j < propertyList.length; j++) {
                var cell = row.insertCell(j);
                cell.innerHTML = residents[propertyList[j]];
            }
            //table.innerHTML += "</tr>";
            var modal = document.getElementById('myModal')
            $('#myModal').modal("show")
        })
    }
    })
    });
});
});
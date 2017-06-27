$(document).ready(function() {
    $("[id=resident]").click(function() {
        var $row = $(this).closest("tr"),        // Finds the closest row <tr> 
    $tds = $row.find("td:nth-child(1)"); // Finds the 1st <td> element
    $.each($tds, function() {                // Visits every single <td> element
    var planetName = $(this).text();         // Prints out the text within the <td>
    $.getJSON('https://swapi.co/api/planets/', function(response) {
    var planetsDatas = response['results'];
    for (var i = 0; i < planetsDatas.length; i ++) {
        if (planetName.includes(planetsDatas[i]['name'])) {
            var residentsLinks = (planetsDatas[i]['residents']);
        }
       };
    console.log(residentsLinks);
    })
    });
});
});
/* var myArray = [
    {'date':'04-01-2021', 'vehicle':'Bear I', 'cost':'$0',},
    {'date':'04-03-2021', 'vehicle':'Orca I', 'cost':'$0'},
    {'date':'04-05-2021', 'vehicle':'Moose I', 'cost':'$0'},
    {'date':'04-10-2021', 'vehicle':'Bear II', 'cost':'$0'},
    {'date':'04-12-2021', 'vehicle':'Bumblebee I', 'cost':'$0'},
    {'date':'04-13-2021', 'vehicle':'Bumblebee II', 'cost':'$0'},
    {'date':'04-14-2021', 'vehicle':'Bumblebee III', 'cost':'$0'},
    {'date':'04-15-2021', 'vehicle':'Bumblebee IV', 'cost':'$0'},
    {'date':'04-20-2021', 'vehicle':'Orca II', 'cost':'$0'},
    {'date':'04-23-2021', 'vehicle':'Moose II', 'cost':'$0'},
    {'date':'04-30-2021', 'vehicle':'Bear III', 'cost':'$0'},
]

*/

var xmlhttp = new XMLHttpRequest();
xmlhttp.open("GET", "data.json", false);
xmlhttp.send(null);
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArray = JSON.parse(this.responseText);
        console.log(myArray);
    }
}

//sorting function
$('th').on('click', function(){
    var column = $(this).data('column')
    var order = $(this).data('order')
    var text = $(this).html()
    text = text.substring(0, text.length - 1)

    if(order == 'desc'){
        $(this).data('order', "asc")
        myArray = myArray.sort((a,b) => a[column] > b[column] ? 1 : -1)
        text += '&#9660'
    }else{
        $(this).data('order', "desc")
        myArray = myArray.sort((a,b) => a[column] < b[column] ? 1 : -1)
        text += '&#9650'
    }
    $(this).html(text)
    buildTable(myArray)
})

buildTable(myArray)

//searching function
$('#search-input').on('keyup', function(){
    var value = $(this).val()
    console.log("Value:", value)

    var data = searchTable(value, myArray)
    buildTable(data)
})

function searchTable(value, data){
    var filteredData = []
    for (var i = 0; i < data.length; i++){
        value = value.toLowerCase()
        var vehicleName = data[i].vehicle.toLowerCase()
        var dateName = data[i].date.toLowerCase()

        if(vehicleName.startsWith(value) || dateName.startsWith(value)){
            filteredData.push(data[i])
        }
    }

    return filteredData
}

//build table from JSON data
function buildTable(data){
    var table = document.getElementById('myTable')

    table.innerHTML = ''
    
    for (var i = 0; i < data.length; i++){
        var row = `<tr>
                        <td>${data[i].date}</td>
                        <td>${data[i].vehicle}</td>
                </tr>`
        table.innerHTML += row
    }
}
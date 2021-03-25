var myArray = []

buildTable(myArray)

$.ajax({
    method:'GET',
    //use the following line if running on a web server
    url:'data.json',
    //use the following line if running locally
    //url:'https://api.jsonbin.io/b/605bd7adb87f462d7aa2ba7c/4',
    success:function(response){
        myArray = response.flights
        buildTable(myArray)
        console.log(myArray)
    }
})

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
    //console.log("Value:", value)

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
                        <td> <button onclick="buildModal(myArray, this.innerText);" type="button" class="btn" data-toggle="modal" data-target="#theModal">${data[i].vehicle}</button></td>
                </tr>`
        table.innerHTML += row
    }
}

function buildModal(table, vehicle){
    var modTable = document.getElementById('modalTable')
    
    modTable.innerHTML = ''

    for (var i = 0; i < table.length; i++){
        if(vehicle === table[i].vehicle){
            var index = i
        }
    }
    
    for (var x in table[index]) {
        var newRow = `<tr>
            <td>${capitalizeWords(x)}</td>    
            <td>${table[index][x]}</td> 
        </tr>`
        modTable.innerHTML += newRow
    }
}

function capitalizeWords(input){
    const sentence = input
    const words = sentence.split(" ");

    for (var i = 0; i < words.length; i++){
        words[i] = words[i][0].toUpperCase() + words[i].substr(1)
    }
    return words.join(" ");
}
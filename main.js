var myArray = []

$.ajax({
    method:'GET',
    //use the following line if running on a local server
    url:'data.json',
    //use the following line if running without a server
    //url:'https://api.jsonbin.io/b/605bd7adb87f462d7aa2ba7c/6',
    success:function(response){
        myArray = response.flights
        buildTable(myArray)
        findSum(myArray)
        console.log(myArray)
    }
})

//sorting function
$('th').on('click', function(){
    if ($(this).data('column') == 'ignore'){
        return
    }
    
    var header = document.getElementById('date')
    var header2 = document.getElementById('vehicle')
    var header3 = document.getElementById('cost')

    if ($(this).data('column') == 'date'){
        header.style.background = "navy"
        header2.style.background = "#007bff"
        header3.style.background = "#007bff"
    }
    if ($(this).data('column') == 'vehicle'){
        header.style.background = "#007bff"
        header2.style.background = "navy"
        header3.style.background = "#007bff"
    }
    if ($(this).data('column') == 'cost'){
        header.style.background = "#007bff"
        header2.style.background = "#007bff"
        header3.style.background = "navy"
    }
    

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

function findSum(data){
    sum = 0
    for (var i = 0; i < data.length; i++){
        sum += isNaN(data[i].cost.substring(1)) ? 0 : parseFloat(data[i].cost.substring(1));
        //console.log(data[i].cost.substring(1))
    }

    //console.log(sum)

    var output = document.getElementById('texthere')
    output.innerHTML += sum;
}

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
                        <td> <button onclick="buildModal(myArray, this.innerText);" type="button" class="btn btn-nopad" data-toggle="modal" data-target="#theModal"><u>${data[i].vehicle}</u></button></td>
                        <td>${data[i].cost}</td>
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
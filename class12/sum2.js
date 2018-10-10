function totalThrough(n) {
    var numbers = new Array(n);
    for (i=0; i < n; i++) {
      numbers[i] = i;
    }
    total = 0;
    for (number of numbers) {
      total += number;
    }
    return total;
}

function getTotal() {
    total = totalThrough(document.getElementById("input").value);
    outputHTML = "The total is <b>" + total + "</b>";
    document.getElementById("output").innerHTML = outputHTML;
}

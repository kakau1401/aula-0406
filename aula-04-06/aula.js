function selectionSort3Numeros(arr) {

    for (let i = 0; i < arr.length - 1; i++) {
      let menor = i;  
    
      for (let j = i + 1; j < arr.length; j++) {
        if (arr[j] < arr[menor]) {
          menor = j; 
        }
      }
    
      if (menor !== i) {
        let temp = arr[i]; 
        arr[i] = arr[menor]; 
        arr[menor] = temp;   
      }
    }
    
    return arr; 
  }
  
  console.log(selectionSort3Numeros([25, 10, 15])); 
  console.log(selectionSort3Numeros([9, 3, 6]));  
  console.log(selectionSort3Numeros([1, 2, 3]));  
  console.log(selectionSort3Numeros([5, 5, 1]));   

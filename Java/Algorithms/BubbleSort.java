public class BubbleSort {
  
	public static int[] swap(int[] arr, int x, int j) {
		int temp = arr[x];
		arr[x] = arr[j];
		arr[j] = temp;
		
		return arr;
	}
	public static void main(String[] args) {
		int[] array = {10,2,9,5,3,4,8,1,7};
		boolean swapped = true;
		while(swapped) {
			swapped = false;
			for(int i = 0; i < array.length - 1; i++){
				if(array[i] > array[i + 1]) {
					swap(array, i, i+1);
					swapped= true;
				}
			}
		}
		
		for(int i : array) {
			System.out.println(i);
		}

	}

}

public class maximumProductofTwoElements {
    public static void main(String[] args) {
        int arr[] = {56, 17, 63, 65, 69};

        int maxProduct = arr[0] * arr[1];
        int index1 = 1; // 1-based index
        int index2 = 2;

        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                int product = arr[i] * arr[j];
                if (product > maxProduct) {
                    maxProduct = product;
                    index1 = i + 1;
                    index2 = j + 1;
                }
            }
        }

        System.out.println("Max Product : " + maxProduct);
        System.out.println("i : " + index1);
        System.out.println("j : " + index2);
    }
}

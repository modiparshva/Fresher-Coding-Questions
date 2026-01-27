public class revStr {
    public static void main(String[] args) {
        String s1 = "Parshva";
        String s2 = "";

        int j = s1.length() - 1;

        while (j >= 0) {
            s2 = s2 + s1.charAt(j);
            j--;
        }

        System.out.println("Reversed String: " + s2);
    }
}

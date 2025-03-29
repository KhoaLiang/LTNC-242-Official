public class Prediction {
    public static void main(String[] args) {
        int[] sequence = {51, 83, 8, 27, 28, 4, 77, 35, 32, 18, 42, 79, 63, 32, 20, 2, 18, 15, 66, 88, 29, 16, 72, 47, 42, 49, 66, 89, 81, 41, 19, 49, 3, 69, 80};
        int nextNumber = predictNextNumber(sequence);
        System.out.println("The next number in the sequence is: " + nextNumber);
    }

    public static int predictNextNumber(int[] sequence) {
        int n = sequence.length;
        int sumOfDifferences = 0;

        // Calculate the sum of differences between consecutive numbers
        for (int i = 1; i < n; i++) {
            sumOfDifferences += sequence[i] - sequence[i - 1];
        }

        // Calculate the average difference
        int averageDifference = sumOfDifferences / (n - 1);

        // Predict the next number
        int nextNumber = (sequence[n - 1] + averageDifference) % 100;

        // Ensure the next number is within the range 00 to 99
        if (nextNumber < 0) {
            nextNumber += 100;
        }

        return nextNumber;
    }
}
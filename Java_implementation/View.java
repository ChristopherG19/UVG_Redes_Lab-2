import java.util.Scanner;

public class View {

    Scanner scan = new Scanner(System.in);

    public View() {}

    public String getUserInput() {
        String input = "";
        boolean gettingInput = true;

        while (gettingInput) {
            System.out.println("Ingrese la secuencia a emitir:");
            String Userinput = scan.nextLine();

            // check for other symbols other tha 0 or 1
            boolean invalidInput = false;
            for (char c: Userinput.toCharArray()) {
                if (c == '0' || c == '1') {
                    // correct
                } else invalidInput = true;
            }

            if (invalidInput){
                // The message contains symbols other than 0 or 1
                System.out.println("\n[INPUT INVALIDO] Pruebe nuevamente\n");
            } else {
                // Correct input

                System.out.println("Desea enviar " + Userinput + " al emisor?: (y/n)");
                String exit = scan.nextLine();

                if (exit.toLowerCase().equals("y")) {
                    // Exit the loop
                    input = Userinput;
                    gettingInput = false;
                } else if (exit.toLowerCase().equals("n")) {
                    System.out.println("Pruebe nuevamente");
                } else {
                    System.out.println("\n[INPUT INVALIDO] Pruebe nuevamente\n");
                }
            }
        }

        return input;
    }
    
}

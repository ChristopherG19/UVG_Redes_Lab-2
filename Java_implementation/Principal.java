import java.util.ArrayList;

public class Principal {
    public static void main(String[] arg) {

        View view = new View();
        

        String input = view.getUserInput();
        System.out.println("user input \n" + input);

        // Give input to emisor
        Emisor emisor = new Emisor(input);
        ArrayList<Boolean> response = emisor.get_response();

        Receptor receptor = new Receptor(response);
        

    }
}

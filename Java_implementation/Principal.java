public class Principal {
    public static void main(String[] arg) {

        View view = new View();
        

        String input = view.getUserInput();
        System.out.println("user input \n" + input);

        // Give input to emisor
        EmisorCRC emisor = new EmisorCRC(input);
        String response = emisor.get_response();

        ReceptorCRC receptor = new ReceptorCRC(response);

        EmisorHam emisorH = new EmisorHam(input);
        

    }
}

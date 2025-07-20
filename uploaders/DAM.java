import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class DAM {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "EAR_TAG,InHerd,NO_OF_LACTS,HOLSTEIN_PERC,FAMILY_NO,GENETIC_GROUP,DAM_CODE,SIRE_CODE,DOB,BOOK_NO";


    public static void main(String[] args) {
        readfile("cleanData/DAM.csv", DAMHEAD);
        System.out.println(data);
        // Open a connection
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected to DB...");

            insertData(conn);


            //Statement stmt = conn.createStatement();
            //String test = "INSERT INTO dam VALUES (1, 1, 1, 1, 1, 1, 1, 1, 1, 11/11/11, 1, 1)";
            //stmt.executeUpdate(test);

            //stmt = conn.createStatement();
            //String sql = "SELECT * from langhillherd.dam";
            //ResultSet set = stmt.executeQuery(sql);
            //printResults(set);
        } catch (Exception e) {
            e.printStackTrace();
       }
    }

    /**
     * Reads in the file and stores it into a static array of Data.
     * @param writefilename
     * @throws SQLException
     */
    private static void readfile(String writefilename, String validator) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(writefilename));
            String line = "";
            // Reads the first line.
            line = reader.readLine();
            // Checks to see if the file is empty, if it is, terminates the program.
            // If the file is not empty, it checks to see if it is in the correct format to be processed, if it is not, then the program terminates.
            //if (!line.equals(validator)) {
                //System.out.println("This file is not in the correct format to be used.");
                //System.out.println("First line is " + line);
                //System.exit(0);
            //}
            // Reads the file and stores the data in a static ArrayList to put the values into the program.
            while ((line = reader.readLine()) != null) {
                data.add(line);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            System.exit(0);
        } catch (IOException e) {
            System.out.println("IO Exception: " + e.getMessage());
            System.exit(0);
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Couldn't close reader: " + e.getMessage());
                    System.exit(0);
                }
            }
        }
    }

    /**
     * Inserts the Data into the table using a batch statement.
     * @param connection
     * @throws SQLException
     */
    private static void insertData(Connection connection) throws SQLException {
        // Creates a prepared statement to insert the data.
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "newdam" + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            //System.out.print(elements[0]);
            int inHerd = Integer.parseInt(elements[1]);
            int NO_OF_LACTS = Integer.parseInt(elements[2]);
            double HOLSTEIN_PERC = Double.parseDouble(elements[3]);
            int FAMILY_NO = -1;
            if (!elements[4].equals("NULL")) {
                FAMILY_NO = Integer.parseInt(elements[4]);
            }
            System.out.println("Family Number is " + FAMILY_NO);
            char GENETIC_GROUP = elements[5].charAt(0);
            int DAM_CODE = Integer.parseInt(elements[6]);
            int SIRE_CODE = Integer.parseInt(elements[7]);
            String DOB = elements[8];
            String dateString = elements[9];
            Date date = null;
            try {
                SimpleDateFormat origDateFormat = new SimpleDateFormat("DD/MM/YYYY hh:mm");
                date = (Date) origDateFormat.parse(DOB);
            } catch (Exception e) {

            }

            long BOOK_NO = Long.parseLong(elements[9]);


            statement.setInt(1, earTag);

            statement.setInt(2, inHerd);
            statement.setInt(3, NO_OF_LACTS);

            statement.setDouble(4, HOLSTEIN_PERC);
            if (FAMILY_NO < 0) {
                System.out.println("Here");
                statement.setNull(5, Types.DOUBLE);
            } else {
                statement.setInt(5, FAMILY_NO);

            }

            statement.setString(6, String.valueOf(GENETIC_GROUP));
            statement.setInt(7, DAM_CODE);
            statement.setInt(8, SIRE_CODE);
            statement.setString(9, DOB);
            statement.setLong(10, BOOK_NO);

            // A batch is used in order to execute all of the inserts at once.

            statement.addBatch();
        }
        // Inserts all of the data at once, commits the data in order to validate the inputs manually.

        System.out.println("hello");
        statement.executeBatch();
        System.out.println("hello");
        //connection.commit();
        statement.close();
    }


    /**
     * Checks to see if a String variable can be parsed as a double.
     * @param tocheck
     * @return
     */
    private static boolean checkDouble(String tocheck) {
        try {
            Double.parseDouble(tocheck);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }


}

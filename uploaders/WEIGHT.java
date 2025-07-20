import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class WEIGHT {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "EAR_TAG,Feed_type,MILK_DATE,LIVE_WGT,MON_WGT,TUE_WGT,WED_WGT,THU_WGT,FRI_WGT,Daily_yeild_wgt";


    public static void main(String[] args) {
        readfile("cleanData/weight.csv", DAMHEAD);
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
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "weight" + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            String Feed_TYPE = elements[1];
            String MILK_DATE = elements[2];
            int LIVE_WGT = -1;
            if (!elements[3].equals("NULL")) {
                LIVE_WGT = Integer.parseInt(elements[3]);
            }
            String MON_WGT = (elements[4]);
            String TUE_WGT = (elements[5]);
            String WED_WGT = (elements[6]);
            String THU_WGT = (elements[7]);
            String FRI_WGT = (elements[8]);
            double Daily_yeild_wgt = -1;
            if (!elements[9].equals("NULL")) {
                Daily_yeild_wgt = Double.parseDouble(elements[9]);
            }




            statement.setInt(1, earTag);
            statement.setString(2, Feed_TYPE);
            statement.setString(3, MILK_DATE);
            if (LIVE_WGT < 0) {
                statement.setNull(4, Types.DOUBLE);
            } else {
                statement.setInt(4, LIVE_WGT);

            }
            statement.setString(5, MON_WGT);
            statement.setString(6, TUE_WGT);
            statement.setString(7, WED_WGT);
            statement.setString(8, THU_WGT);
            statement.setString(9, FRI_WGT);
            if (Daily_yeild_wgt < 0) {
                statement.setNull(10, Types.DOUBLE);
            } else {
                statement.setDouble(10, Daily_yeild_wgt);

            }

            // A batch is used in order to execute all of the inserts at once.

            statement.addBatch();
        }
        // Inserts all of the data at once, commits the data in order to validate the inputs manually.

        System.out.println("hello");
        statement.executeBatch();

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

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class Water_Intakes {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "Ear_Tag,Lact_no,Trough_No,start_time,stop_time,stop_wgt,start_wgt,Consumed,entry_no,start_time_mon,start_time_tue,start_time_wed,start_time_thu,start_time_fri";


    public static void main(String[] args) {
        readfile("cleanData/WATER_INTAKES2.csv", DAMHEAD);
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
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "waterintakes_day" + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            //System.out.print(elements[0]);
            int LACT_NO = Integer.parseInt(elements[1]);
            int TROUGH_NO = Integer.parseInt(elements[2]);
            String START_TIME = (elements[3]);
            String STOP_TIME = (elements[4]);
            
            double STOP_WGT = Double.parseDouble(elements[5]);
            double START_WGT = Double.parseDouble(elements[6]);
            double CONSUMED = Double.parseDouble(elements[7]);
            int ENTRY_NO = Integer.parseInt(elements[8]);
            String START_TIME_MON = (elements[9]);
            String START_TIME_TUE = (elements[10]);
            String START_TIME_WED = (elements[11]);
            String START_TIME_THU = (elements[12]);
            String START_TIME_FRI = (elements[13]);


            statement.setInt(1, earTag);

            statement.setInt(2, LACT_NO);
            statement.setInt(3, TROUGH_NO);

            statement.setString(4, START_TIME);
            statement.setString(5, STOP_TIME);
            statement.setDouble(6, STOP_WGT);
            statement.setDouble(7, START_WGT);
            statement.setDouble(8, CONSUMED);
            statement.setInt(9, ENTRY_NO);
            statement.setString(10, START_TIME_MON);
            statement.setString(11, START_TIME_TUE);
            statement.setString(12, START_TIME_WED);
            statement.setString(13, START_TIME_THU);
            statement.setString(14, START_TIME_FRI);
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

import java.io.*;
import java.util.*;

public class Bot {

    public static void main(String[] args) {
        Scanner sin = new Scanner(System.in);
        int n_input = sin.nextInt();
        char grid[][]= new char [n_input][n_input];
//         reading the matrix 
        for(int i =0;i<n_input;i++){
            for(int j=0;j<n_input;j++){
                grid[i][j] =  sin.next                
            }
        }
//         get the location of the princess and bot
        int B_x = 0, B_y =0;
        int P_x = 0, P_y =0;
        int c_breaker = 0;
        for(int i =0;i<n_input;i++){
            for(int j=0;j<n_input;j++){
                if(grid[i][j]=='m'){
                    B_x = i;
                    B_y = j;
                    c_breaker++;
                } 
                else if(grid[i][j]=='p'){
                    P_x = i;
                    P_y = j;
                    c_breaker++;
                }
            }
                                if(c_breaker==2){
                                    break;
                                }
        }
                                System.out.println("bot x and y "+B_x+" "+B_y+"\n pricess x and y "+P_x+" "+P_y);
            
        
        
    }
}
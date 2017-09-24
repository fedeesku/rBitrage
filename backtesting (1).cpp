//MHacks X 2017 rBitrage
//Backtesting ML algorithm over the past month of September data
//NOTE: THIS SEPTEMBER DATA HAS NOT BEEN TRAINED INTO NEURAL NETWORK

#include <iostream>
#include <cmath>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

void blackBox(double currentBTC);
//Used to determine the next step
bool buyETH;
bool sellETH;
//quantity of ETH and BTC
double quantityETH;
double quantityCash;
//Establish the spreadsheet variables
int timeETHOriginal;
int timeBTCOriginal;
double lowETHOriginal;
double lowBTCOriginal;
double highETHOriginal;
double highBTCOriginal;
double openETHOriginal;
double openBTCOriginal;
double closeETHOriginal;
double closeBTCOriginal;
double volumeETHOriginal;
double volumeBTCOriginal;
//Next Values
int timeETHNext;
int timeBTCNext;
double lowETHNext;
double lowBTCNext;
double highETHNext;
double highBTCNext;
double openETHNext;
double openBTCNext;
double closeETHNext;
double closeBTCNext;
double volumeETHNext;
double volumeBTCNext;


int main() {
    //Initalize BUY/SELL
    sellETH = false;
    buyETH = false;
    //Initalize quantities
    quantityCash = 10000;
    quantityETH = 0;
    //Read in September Data
    ifstream input("SeptemberDatatext.txt");
    input >> timeETHOriginal >> lowETHOriginal >> highETHOriginal >> openETHOriginal >> closeETHOriginal >> volumeETHOriginal >> timeBTCOriginal >> lowBTCOriginal >> highBTCOriginal >> openBTCOriginal >> closeBTCOriginal >> volumeBTCOriginal;
    if (input.is_open()){
        while (input >> timeETHNext >> lowETHNext >> highETHNext >> openETHNext >> closeETHNext >> volumeETHNext >> timeBTCNext >> lowBTCNext >> highBTCNext >> openBTCNext >> closeBTCNext >> volumeBTCNext){
            blackBox(openBTCOriginal);
            //Determine Investment Amount
            //Backtest
            //Update Holdings
            //Reset Next to Original for next iteration
            timeETHOriginal = timeETHNext;
            timeBTCOriginal = timeBTCNext;
            lowETHOriginal = lowETHNext;
            lowBTCOriginal = lowBTCNext;
            highETHOriginal = highETHNext;
            highBTCOriginal = highBTCNext;
            openETHOriginal = openETHNext;
            openBTCOriginal = openBTCNext;
            closeETHOriginal = closeETHNext;
            closeBTCOriginal = closeBTCNext;
            volumeETHOriginal = volumeETHNext;
            volumeBTCOriginal = volumeBTCNext;
        }
    }
    else {
        cout <<"There was an error reading the September Data file" << endl;
    }
    cout << "Closing Cash $" << quantityCash << endl;
    cout << "Closing Quantity of ETH " << quantityETH << endl;
    cout << "Closing Price of ETH $" <<  closeETHNext << endl;
    cout << "Closing Amount of Holdings $" << (quantityCash + quantityETH * closeETHNext) << endl;
    double percentReturns = ((quantityCash + quantityETH * closeETHNext)-10000)/ 10000 * 100;
    cout << "Backtesting algorithm provides " << percentReturns << "% for month of September";
    return 0;
}

void blackBox(double currentBTC){
    //stil needs to be impletmented
   /*
    if (){
        buyETH = true;
    }
    else {
        buyETH = false;
    }
    //cout << buyETH << endl;
   // cout << buyETH << endl;
    if (buyETH == true && quantityCash > 0){
        cout << "We bought" << endl;
        quantityETH = ((quantityCash/500)/openETHOriginal) + quantityETH;
        quantityCash = quantityCash - (quantityCash/500);
    }
    else if (buyETH == false && quantityETH > 0){
       double qs = 0.5*quantityETH;
        quantityETH = quantityETH - qs;
        quantityCash = quantityCash + (qs * openETHOriginal);
    }
    */
}

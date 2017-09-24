//
//  ViewController.swift
//  rBitrage
//
//  Created by Pinto Bean on 9/24/17.
//  Copyright © 2017 Nikki Duran. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var btcColor: UIView!
    @IBOutlet var ethColor: UIView!
    @IBOutlet var bitcoinPrice: UILabel!
    @IBOutlet var ethereumPrice: UILabel!
    @IBOutlet var eth5Confidence: UILabel!
    @IBOutlet var eth30Confidence: UILabel!
    @IBOutlet var eth60Confidence: UILabel!
    @IBOutlet var btcPercent: UILabel!
    @IBOutlet var ethPercent: UILabel!
    
    var refreshTimer = Timer()
    let btcGradientLayer = CAGradientLayer()
    let ethGradientLayer = CAGradientLayer()
    
    @objc func refreshPrice() {
        let oldETHPrice = 0;
        let oldBTCPrice = 0;
        if let url = URL(string: ("https://api.coinbase.com/v2/prices/spot?currency=USD")) {
            let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
                
                if error != nil {
                    
                    print(error)
                    
                } else {
                    
                    if let urlContent = data {
                        do {
                            let jsonResult = try JSONSerialization.jsonObject(with: urlContent, options: JSONSerialization.ReadingOptions.mutableContainers) as AnyObject
                            
                            print("json result:")
                            print(jsonResult)
                            
                            print(jsonResult["data"])
                            
                            if let price = ((jsonResult["data"]) as? NSDictionary)?["amount"] as? String {
                                DispatchQueue.main.sync(execute: {
                                    var myString = self.bitcoinPrice.text
                                    if (myString?.contains("$"))! {
                                        myString?.removeFirst()
                                    }
                                    let numFormat = (myString! as NSString).doubleValue
                                    print("oldprice")
                                    print(numFormat)
                                    let numFormat2 = (price as NSString).doubleValue
                                    print("newprice")
                                    print(numFormat2)
                                    let percentChange = (numFormat2 - numFormat)*100/(numFormat)
                                    if (numFormat > numFormat2){
                                        self.btcColor.backgroundColor = UIColor.red
                                        self.btcGradientLayer.frame = self.btcColor.bounds
                                        let color1 = UIColor(white: 0.0, alpha: 0.3).cgColor as CGColor
                                        let color2 = UIColor(white: 0.7, alpha: 0.2).cgColor as CGColor
                                        self.btcGradientLayer.colors = [color1, color2]
                                        self.btcGradientLayer.locations = [0.25, 0.75]
                                        self.btcColor.layer.addSublayer(self.btcGradientLayer)
                                        if (numFormat > 0) {
                                            self.btcPercent.text = "(" + String(percentChange) + "%)"
                                        } else {
                                            self.btcPercent.text = "(- 0.00 %)"
                                        }
                                    }
                                    else if (numFormat2 > numFormat){
                                        self.btcColor.backgroundColor = UIColor.green
                                        self.btcGradientLayer.frame = self.btcColor.bounds
                                        let color1 = UIColor(white: 0.0, alpha: 0.3).cgColor as CGColor
                                        let color2 = UIColor(white: 0.7, alpha: 0.2).cgColor as CGColor
                                        self.btcGradientLayer.colors = [color1, color2]
                                        self.btcGradientLayer.locations = [0.25, 0.75]
                                        self.btcColor.layer.addSublayer(self.btcGradientLayer)
                                        if (numFormat > 0) {
                                            self.btcPercent.text = "(+ " + String(percentChange) + "%)"
                                        } else {
                                            self.btcPercent.text = "(+ 0.00 %)"
                                        }
                                    }
                                    self.bitcoinPrice.text = "$" + price
                                })
                            }
                            
                        } catch {
                            
                            print("JSON Processing Failed")
                        }
                    }
                }
            }
            task.resume()
        }
        
        if let url2 = URL(string: ("https://api.gdax.com/products/ETH-USD/ticker")) {
            let task2 = URLSession.shared.dataTask(with: url2) { (data, response, error) in
                if error != nil {
                    
                    print(error)
                    
                } else {
                    
                    if let urlContent = data {
                        do {
                            let jsonResult = try JSONSerialization.jsonObject(with: urlContent, options: JSONSerialization.ReadingOptions.mutableContainers) as AnyObject
                            
                            print("json result:")
                            print(jsonResult)
                            
                            print(jsonResult["price"])
                            
                            if let price = (jsonResult["price"]) as? String {
                                DispatchQueue.main.sync(execute: {
                                    var myString = self.ethereumPrice.text
                                    if (myString?.contains("$"))! {
                                        myString?.removeFirst()
                                    }
                                    let numFormat = (myString! as NSString).doubleValue
                                    print("oldprice")
                                    print(numFormat)
                                    let numFormat2 = (price as NSString).doubleValue
                                    print("newprice")
                                    print(numFormat2)
                                    let percentChange = (numFormat2 - numFormat)*100/(numFormat)
                                    if (numFormat > numFormat2){
                                        self.ethColor.backgroundColor = UIColor.red
                                        self.ethGradientLayer.frame = self.ethColor.bounds
                                        let color1 = UIColor(white: 0.0, alpha: 0.3).cgColor as CGColor
                                        let color2 = UIColor(white: 0.7, alpha: 0.2).cgColor as CGColor
                                        self.ethGradientLayer.colors = [color1, color2]
                                        self.ethGradientLayer.locations = [0.25, 0.75]
                                        self.ethColor.layer.addSublayer(self.ethGradientLayer)
                                        if (numFormat > 0) {
                                            self.ethPercent.text = "(" + String(percentChange) + "%)"
                                        } else {
                                            self.ethPercent.text = "(- 0.00 %)"
                                        }
                                    }
                                    else if (numFormat2 > numFormat){
                                        self.ethColor.backgroundColor = UIColor.green
                                        self.ethGradientLayer.frame = self.ethColor.bounds
                                        let color1 = UIColor(white: 0.0, alpha: 0.3).cgColor as CGColor
                                        let color2 = UIColor(white: 0.7, alpha: 0.2).cgColor as CGColor
                                        self.ethGradientLayer.colors = [color1, color2]
                                        self.ethGradientLayer.locations = [0.25, 0.75]
                                        self.ethColor.layer.addSublayer(self.ethGradientLayer)
                                        if (numFormat > 0) {
                                            self.ethPercent.text = "(+ " + String(percentChange) + "%)"
                                        } else {
                                            self.ethPercent.text = "(+ 0.00 %)"
                                        }
                                    }
                                    self.ethereumPrice.text = "$" + price
                                    
                                })
                            }
                            
                        } catch {
                            
                            print("JSON Processing Failed")
                        }
                    }
                }
            }
            task2.resume()
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        self.refreshPrice()
        refreshTimer = Timer.scheduledTimer(timeInterval: 10.0, target: self, selector: #selector(ViewController.refreshPrice), userInfo: nil, repeats: true)
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


//
//  ViewController.swift
//  iPhoneCall
//
//  Created by Chetan J. Giridhar on 16/05/15.
//  Copyright (c) 2015 Chetan J. Giridhar. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var bgImage: UIImageView!
    @IBOutlet weak var broadcastButton: UIButton!
    
    var httpObj = http()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBOutlet weak var numberLabel: UITextField!
    
    @IBAction func smsButton() {
        var number = numberLabel.text
        //println("In SMS")
        httpObj.post(
            ["number": number],
            url: "http://127.0.0.1:5000/sms")
    }
    
    @IBAction func callButton() {
        var number = numberLabel.text
        //println("In Call")
        httpObj.post(["number": number],
            url: "http://127.0.0.1:5000/callout")
    }
    

    @IBAction func callCell3() {
        var number = numberLabel.text
        //println("In Call")
        httpObj.post(["number": "+919886509613"],
            url: "http://127.0.0.1:5000/callout")
    }
    

    @IBAction func broadCastAction() {
        httpObj.post(["number": "+919886509613"],
            url: "http://127.0.0.1:5000/callout")
        httpObj.post(["number": "+919422095704"],
            url: "http://127.0.0.1:5000/callout")
    }

}


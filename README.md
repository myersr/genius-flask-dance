# genius-flask-dance
A simple [Flask](http://flask.pocoo.org/) server that authenticates a user with their [Genius.com](https://genius.com/) account.  
The application uses [Flask-dance's](lask-dance.readthedocs.io/en/latest) custom blueprint to authenticate through Oauth2.


## Installing

A step by step series of examples that tell you have to get a development env running. With python I Always suggest a virtual environment.  


Install the python packages

```
pip install -r requirements.txt
```  

To run the server run
```  
python server.py
```   
__Note:__ to run the Oauth authentication without an ssl certificate run this: `export OAUTHLIB_INSECURE_ANSPORT=1`



## Authors

* **Roy Myers** - *Initial work* - [rmyers19](https://github.optum.com/rmyers19)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

----
## Links and Thanks!
[Genius.com](https://genius.com/)
[Flask](http://flask.pocoo.org/)
[Flask-dance's](lask-dance.readthedocs.io/en/latest)


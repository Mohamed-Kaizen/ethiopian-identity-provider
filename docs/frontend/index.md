# FrontEnd

## Getting Started

* [Fork repository][Ethiopian Identity Provider] and clone it.

=== "Shell or CMD"
    <div class="termy">
    ```console
    $ git clone https://github.com/Mohamed-Kaizen/ethiopian-identity-provider-FrontEnd/
    
    ---> 100%

    Done :)
    ```
    </div>

### install dependence

=== "Yarn"
    <div class="termy">
    ```console
    $ cd ethiopian-identity-provider
    $ yarn install
    
    Resolving dependencies... 
    ---> 100%

    Writing lock file

    Done :)
    ```
    </div>

=== "Npm"
    <div class="termy">
    ```console
    $ cd ethiopian-identity-provider
    $ npm install
    
    Resolving dependencies... 
    ---> 100%

    Writing lock file

    Done :)
    ```
    </div>

### Running server

=== "Yarn"
    <div class="termy">
    ```console
    $ yarn dev
    run-p watch:tailwind dev:sapper
    sapper dev
    postcss static/tailwind.css -o static/index.css -w
    > Listening on http://localhost:3000

    ```
    </div>

=== "Npm"
    <div class="termy">
    ```console
    $ npm run dev
    run-p watch:tailwind dev:sapper
    sapper dev
    postcss static/tailwind.css -o static/index.css -w
    > Listening on http://localhost:3000

    ```
    </div>


[Ethiopian Identity Provider]: https://github.com/Mohamed-Kaizen/ethiopian-identity-provider-FrontEnd/

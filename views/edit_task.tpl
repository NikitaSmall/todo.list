<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Python todo</title>

    <!-- Bootstrap -->
    <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
  <div class="container">
    <div class="row">
        <h2>Задачки от Бутылки для Никитки!</h2>
        <p class="text-right">Никитка, редактируй хорошо! Тебе это ещё выполнять.</p>
        <form action="/edit/{{no}}" method="POST">
            <div class="form-group">

                <input type="text" size="255" maxlength="255" name="task" class="form-control" value="{{data[0]}}">
            </div>
            <div class="form-group">
                <select name="status" class="form-control">
                    <option value="1"
                            %if data[1] == 1:
                            selected
                            %end
                            >Открыто</option>
                    <option value="0"
                            %if data[1] == 0:
                            selected
                            %end
                            >Закрыто</option>
                </select>
            </div>
            <input type="submit" name="save" value="Изменить!" class="btn btn-default">
        </form>
    </div>
  </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/js/bootstrap.min.js"></script>
  </body>
</html>
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
        <div class="text-warning">
            %if message == 'added':
                Новое задание добавлено!
            %end

        </div>
        <p class="text-right">Никитка, перед тобой список твоих задач. Ты должен выполнить их!</p>
        <table class="table table-striped">
        %for row in rows:
          <tr>
            <td><input type="checkbox" name="task[{{row[0]}}]" value="1"
                    %if row[2] == 0:
                        checked
                    %end
                    /> </td>
              <td>{{row[1]}}</td>
              <td class="text-right"><a href="/edit/{{row[0]}}" class="btn btn-info"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a></td>
              <td class="text-right">
                  <form method="DELETE" action="/delete/{{row[0]}}">
                      <button type="submit" class="btn btn-danger">
                          <span class="glyphicon glyphicon-trash" aria-hidden="true"></span>
                      </button>
                  </form>
                  <!--<a href="/delete/{{row[0]}}" class="btn btn-danger"></a>-->
              </td>
          </tr>
        %end
        </table>

        <br />
        <a href="/new" class="btn btn-primary">Новая задача!</a>
    </div>
  </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/js/bootstrap.min.js"></script>
  </body>
</html>
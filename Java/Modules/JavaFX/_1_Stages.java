import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.input.KeyCombination;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class _1_Stages extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        Group rootNode = new Group();
        Scene scene = new Scene(rootNode, Color.BLACK);
        stage.setTitle("BurnKnuckle");
        Image icon = new Image("BurnKnuckle.png");
        stage.getIcons().add(icon);
        stage.setWidth(400);
        stage.setHeight(400);
        stage.setResizable(false);
        stage.setX(50);
        stage.setY(50);
        stage.setFullScreen(true);
        stage.setFullScreenExitHint("You cant escape until you press q");
        stage.setFullScreenExitKeyCombination(KeyCombination.valueOf("q"));
        stage.setScene(scene);
        stage.show();
    }
}
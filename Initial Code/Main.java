public class Main {
    public static void main(String[] args) {
        Battle.moveRandomGround();
        Combatable[] team1 = TeamMaker.makeTeam1();
        Combatable[] team2 = TeamMaker.makeTeam2();
        Battle battle = new Battle(team1, team2);
        battle.combat();
    }
}
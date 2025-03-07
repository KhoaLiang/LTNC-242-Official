import static util.Utility.isSquare;
public class Knight extends Fighter {
    public Knight(int baseHp, int wp) {
        super(baseHp, wp);
    }

    @Override
    public double getCombatScore() {
        if(isSquare(Battle.GROUND) == true){
            if ((getBaseHp() * 2) > 999) {
                return 999;
            }
            return getBaseHp() * 2;
        }
        if(getWp() == 1.0){
            if (getBaseHp() > 999) {
                return 999;
            }
            return getBaseHp();
        }
        if ((getBaseHp() / 10) > 999) {
            return 999;
        }
        return getBaseHp() / 10;
    }
}

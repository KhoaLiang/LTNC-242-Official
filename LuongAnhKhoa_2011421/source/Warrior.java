import static util.Utility.isPrime;
public class Warrior extends Fighter {
    public Warrior(int baseHp, int wp) {
        super(baseHp, wp);
    }

    @Override
    public double getCombatScore() {
        if(isPrime(Battle.GROUND) == true){
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

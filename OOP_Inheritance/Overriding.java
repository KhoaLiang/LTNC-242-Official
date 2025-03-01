class Person {
	private String name;
	private String gender;

	public Person(String name, String gender) {
		this.name = name;
		this.gender = gender;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public void display() {
		System.out.println("Name: " + name);
		System.out.println("Gender: " + gender);
	}
}

class Student extends Person {
    private int Salary;
    public Student(String name, String gender, int Salary){
        super(name, gender);
        this.Salary = Salary;
    }
    @Override
    public void display() {
		System.out.println("Name: " + getName());
		System.out.println("Gender: " + getGender());
        System.out.print("Salary: " + Salary);
	}
}

public class Overriding {
	public static void main(String[] args) {
		Student s = new Student("Trung", "Male", 1700);
		s.display();
	}
}
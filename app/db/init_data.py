def init_db():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.db.models import Desk, Employee, OccupancyData
    from app.db.database import get_db_session

    # Create a new database session
    session = get_db_session()

    # Sample data for desks
    desks = [
        Desk(location="Near Cafeteria", features="Standing Desk", area_mapping="Area 1"),
        Desk(location="Quiet Zone", features="Ergonomic Chair", area_mapping="Area 2"),
        Desk(location="Collaboration Space", features="Large Table", area_mapping="Area 3"),
    ]

    # Sample data for employees
    employees = [
        Employee(name="Alice", preferences="Standing Desk"),
        Employee(name="Bob", preferences="Quiet Zone"),
        Employee(name="Charlie", preferences="Collaboration Space"),
    ]

    # Sample occupancy data
    occupancy_data = [
        OccupancyData(area="Area 1", is_occupied=False),
        OccupancyData(area="Area 2", is_occupied=True),
        OccupancyData(area="Area 3", is_occupied=False),
    ]

    # Add desks to the session
    session.add_all(desks)
    session.add_all(employees)
    session.add_all(occupancy_data)

    # Commit the session to save data
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    init_db()
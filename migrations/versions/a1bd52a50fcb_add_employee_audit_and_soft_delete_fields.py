def downgrade() -> None:
    op.drop_index("ix_employees_is_active", table_name="employees")
    op.drop_column("employees", "updated_at")
    op.drop_column("employees", "created_at")
    op.drop_column("employees", "is_active")